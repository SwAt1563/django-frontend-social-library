from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import CommentForm, StarForm, PostForm, PostUpdateForm
from django.http import Http404
from .api.get_post_api import get_post
from .api.create_comment_api import create_comment
from .api.star_api import create_star, remove_star
from .api.update_post_api import update_post
from .api.create_post_api import create_post_api
from .api.delete_post_api import delete_post_api
# Create your views here.


def index(request, post_slug):
    profile_slug = request.session.get('profile_slug')
    post_user_username = request.session.get('username')
    post = None
    try:
        response_status, data = get_post(request, post_slug)
    except Http404:
        raise Http404

    if response_status == 200:
        post = data

    star_form = StarForm
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        star = request.POST.get('star')
        unlike = request.POST.get('unlike')
        if star and str(star) == 'yes':
            payload = dict(
                user_id=request.session.get('user_id'),
                post_slug=post_slug,
            )

            try:
                response_status = create_star(request, payload=payload)
            except Http404:
                raise Http404

            return HttpResponseRedirect(reverse('post:index', kwargs={'post_slug': post_slug, }))
        elif unlike and str(unlike) == 'no':
            payload = dict(
                user_id=request.session.get('user_id'),
                post_slug=post_slug,
            )

            try:
                response_status = remove_star(request, payload=payload)
            except Http404:
                raise Http404

            return HttpResponseRedirect(reverse('post:index', kwargs={'post_slug': post_slug, }))
        elif comment_form.is_valid():

            payload = dict(
                comment=comment_form.cleaned_data['comment'],
                user_id=request.session.get('user_id'),
                post_slug=post_slug,
            )

            try:
                response_status = create_comment(request, payload=payload)
            except Http404:
                raise Http404

            return HttpResponseRedirect(reverse('post:index', kwargs={'post_slug': post_slug,}))
    else:
        comment_form = CommentForm



    return render(request, 'post/index.html', {'profile_slug': profile_slug,
                                               'comment_form': comment_form,
                                               'star_form': star_form,
                                               'post_slug': post_slug,
                                               'post': post,
                                               'post_user_username': post_user_username,
                                               'is_admin': request.session.get('is_admin')})


def create_post(request):
    profile_slug = request.session.get('profile_slug')
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            title = post_form.cleaned_data['title']
            description = post_form.cleaned_data['description']
            payload = dict(
                user_id=request.session.get('user_id'),
                title=title,
                description=description,
            )
            if post_form.cleaned_data.get('image'):
                image = post_form.cleaned_data.get('image')
                payload.update({'file': image})

            else:
                pdf = post_form.cleaned_data.get('pdf')
                payload.update({'file': pdf})

            try:
                response_status = create_post_api(request, payload=payload)
            except Http404:
                raise Http404

            return HttpResponseRedirect(reverse('home:index'))
    else:
        post_form = PostForm
    return render(request, 'post/create_post.html', {'profile_slug': profile_slug,
                                                     'post_form': post_form,
                                                     'is_admin': request.session.get('is_admin'),})

# just for update the title or description
def edit_post(request, post_slug):
    profile_slug = request.session.get('profile_slug')
    try:
        response_status, data = get_post(request, post_slug)
    except Http404:
        raise Http404
    post = {}
    if response_status == 200:
        post = data

    if not post:
        raise Http404
    # just the post owner can edit it
    if post['username'] != request.session.get('username'):
        return HttpResponseRedirect(reverse('home:index'))

    if request.method == 'POST':
        post_update_form = PostUpdateForm(request.POST)
        if post_update_form.is_valid():
            title = post_update_form.cleaned_data['title']
            description = post_update_form.cleaned_data['description']

            payload = dict(
                user_id=request.session.get('user_id'),
                title=title,
                description=description,
            )

            try:
                response_status = update_post(request, post_slug, payload=payload)
            except Http404:
                raise Http404

            return HttpResponseRedirect(reverse('post:index', kwargs={'post_slug': post_slug}))
    else:
        title = post.get('title', '')
        description = post.get('description', '')
        post_update_form = PostUpdateForm(initial={'title': title, 'description': description})

    return render(request, 'post/edit_post.html', {'post_slug': post_slug,
                                                   'profile_slug': profile_slug,
                                                   'post_updated_form': post_update_form,
                                                   'is_admin': request.session.get('is_admin'),})


def delete_post(request, post_slug):
    if request.method == 'GET':
        try:
            payload = dict(
                user_id=request.session.get('user_id')
            )
            response_status = delete_post_api(request, post_slug, payload=payload)
        except Http404:
            raise Http404
        return HttpResponseRedirect(reverse('home:index'))
    raise Http404