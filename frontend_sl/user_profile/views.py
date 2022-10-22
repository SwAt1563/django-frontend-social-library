from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .forms import PersonalImageForm, ProfileEditForm
from django.core.files.storage import FileSystemStorage
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import Http404
from django.http import JsonResponse
from .api.get_profile_api import get_profile
from .api.edit_profile import update_profile, update_profile_image
from .api.follow_unfollow_api import follow_api, unfollow_api
from .api.get_profile_posts import get_profile_posts




def load_more(request, profile_slug):
    posts = []
    try:
        payload = dict(
            posts_owner_slug=profile_slug,
        )
        response_status, data = get_profile_posts(request, payload=payload)
    except Http404:
        raise Http404

    if response_status == 200:
        posts = data

    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 2
    post_obj = list(posts[offset_int:offset_int + limit])
    data = {
        'posts': post_obj
    }

    return JsonResponse(data=data)


def profile(request, profile_slug):
    current_user_profile_slug = request.session.get('profile_slug')
    current_user_username = request.session.get('username')

    profile = None
    try:
        response_status, data = get_profile(request, profile_slug)
    except Http404:
        raise Http404

    if response_status == 200:
        profile = data

    posts = []
    try:
        payload = dict(
            posts_owner_slug=profile_slug,
        )
        response_status, data = get_profile_posts(request, payload=payload)
    except Http404:
        raise Http404

    if response_status == 200:
        posts = data

    post_obj = posts[0:3]
    total_obj = len(posts)


    return render(request, 'user_profile/profile.html', {'profile_slug': current_user_profile_slug, 'posts': post_obj,
                                                         'total_obj': total_obj, 'profile': profile,
                                                         'user_username': current_user_username,
                                                         'is_admin': request.session.get('is_admin')})


'''
we should check if the current user who enter this page same as user
'''


@xframe_options_exempt
def edit_profile(request, profile_slug):
    profile = None
    try:
        response_status, data = get_profile(request, profile_slug)
    except Http404:
        raise Http404

    if response_status == 200:
        profile = data

    if not profile:
        raise Http404

    # just the profile owner can edit it
    if profile['user']['username'] != request.session.get('username'):
        return HttpResponseRedirect(reverse('home:index'))

    # take the user data from the api
    user_profile_img = profile['image']
    user_profile_data = {
        'firstname': profile['user']['first_name'],
        'lastname': profile['user']['last_name'],
        'age': profile['age'],
        'phone': profile['phone'],
        'address': profile['address'],
        'status': profile['status'],
        'about_me': profile['about_me'],
    }
    if request.method == 'POST':
        image_form = PersonalImageForm(request.POST, request.FILES)
        profile_form = ProfileEditForm(request.POST)
        if image_form.is_valid():
            image = request.FILES['image']

            with image.open('rb') as f:
                image = (f.name, f.file.getvalue(), f.content_type)
                payload = dict(
                    user_id=request.session.get('user_id'),
                    image=image,
                )
                try:
                    response_status = update_profile_image(request, profile_slug, payload=payload)
                except Http404:
                    raise Http404

            f.close()

            '''
            Send image to api
            '''

            return HttpResponseRedirect(reverse('user_profile:edit_profile', kwargs={'profile_slug': profile_slug}))
        if profile_form.is_valid():

            payload = {
                'user.first_name': profile_form.cleaned_data.get('firstname'),
                'user.last_name': profile_form.cleaned_data.get('lastname'),
                'age': profile_form.cleaned_data.get('age'),
                'phone': profile_form.cleaned_data.get('phone'),
                'address': profile_form.cleaned_data.get('address'),
                'status': profile_form.cleaned_data.get('status'),
                'about_me': profile_form.cleaned_data.get('about_me'),

                'user_id': request.session.get('user_id'),
            }

            try:
                response_status = update_profile(request, profile_slug, payload=payload)
            except Http404:
                raise Http404
            return HttpResponseRedirect(reverse('user_profile:edit_profile', kwargs={'profile_slug': profile_slug}))

    else:
        image_form = PersonalImageForm()
        profile_form = ProfileEditForm(initial=user_profile_data)

    return render(request, 'user_profile/edit.html', {'profile_slug': profile_slug,
                                                      'image_form': image_form,
                                                      'profile_form': profile_form,
                                                      'user_profile_img': user_profile_img,
                                                      'is_admin': request.session.get('is_admin')})


def follow(request, related_profile_slug):
    if request.method == 'GET':
        try:
            payload = dict(
                user_id=request.session.get('user_id'),
                following_user_slug=related_profile_slug,
            )
            response_status = follow_api(request, payload=payload)
        except Http404:
            raise Http404
        return HttpResponseRedirect(request.GET.get('next'))
    raise Http404


def unfollow(request, related_profile_slug):
    if request.method == 'GET':
        try:
            payload = dict(
                user_id=request.session.get('user_id'),
                following_user_slug=related_profile_slug,
            )
            response_status = unfollow_api(request, payload=payload)
        except Http404:
            raise Http404
        return HttpResponseRedirect(request.GET.get('next'))
    raise Http404
