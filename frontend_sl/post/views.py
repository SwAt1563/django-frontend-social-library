from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import CommentForm, StarForm, PostForm, PostUpdateForm
from django.http import Http404

# Create your views here.


def index(request, post_slug):
    user_slug = 'x'
    star_form = StarForm
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        star = request.POST.get('star')
        unlike = request.POST.get('unlike')
        if star and str(star) == 'yes':
            '''
            pulse one star to this comment by api
            '''
            return HttpResponseRedirect(reverse('post:index', kwargs={'post_slug': post_slug, }))
        elif unlike and str(unlike) == 'no':
            '''
             minus one star to this comment by api
            '''
            return HttpResponseRedirect(reverse('post:index', kwargs={'post_slug': post_slug, }))
        elif comment_form.is_valid():
            comment = comment_form.cleaned_data['comment']
            '''
             send the comment to api with current user to user of the post
            '''
            return HttpResponseRedirect(reverse('post:index', kwargs={'post_slug': post_slug,}))
    else:
        comment_form = CommentForm


    return render(request, 'post/index.html', {'user_slug': user_slug,
                                               'comment_form': comment_form,
                                               'star_form': star_form,
                                               'post_slug': post_slug,})


def create_post(request):
    user_slug = 'x'
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            title = post_form.cleaned_data['title']
            description = post_form.cleaned_data['description']
            if post_form.cleaned_data.get('image'):
                image = post_form.cleaned_data.get('image')
            else:
                pdf = post_form.cleaned_data.get('pdf')
            '''
             create the post by api and get it post_slug
            '''
            post_slug = 'y'

            return HttpResponseRedirect(reverse('home:index'))
    else:
        post_form = PostForm
    return render(request, 'post/create_post.html', {'user_slug': user_slug,
                                                     'post_form': post_form,})

# just for update the title or description
def edit_post(request, post_slug):
    user_slug = 'x'
    if request.method == 'POST':
        post_update_form = PostUpdateForm(request.POST)
        if post_update_form.is_valid():
            title = post_update_form.cleaned_data['title']
            description = post_update_form.cleaned_data['description']

            '''
             create the post by api and get it post_slug
            '''
            post_slug = 'y'

            return HttpResponseRedirect(reverse('post:index', kwargs={'post_slug': post_slug}))
    else:
        # get the initial data from the api
        post_update_form = PostUpdateForm(initial={'title': 'xx', 'description': 'asasasas'})

    return render(request, 'post/edit_post.html', {'post_slug': post_slug,
                                                   'user_slug': user_slug,
                                                   'post_updated_form': post_update_form,})


def delete_post(request, post_slug):
    if request.method == 'GET':
        '''
         send request to api for delete this post
        '''
        return HttpResponseRedirect(reverse('home:index'))
    raise Http404