from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .forms import PersonalImageForm, ProfileEditForm
from django.core.files.storage import FileSystemStorage
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import Http404
from django.http import JsonResponse

# Create your views here.
api_values = [i for i in range(6)]


def load_more(request, user_slug):
    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 2
    # post_obj = Post.objects.all()[offset_int:offset_int+limit]
    post_obj = list(api_values[offset_int:offset_int+limit])
    data = {
        'posts': post_obj
    }

    return JsonResponse(data=data)



def profile(request, user_slug):
    post_obj = api_values[0:5]
    total_obj = len(api_values)
    notifications = [i for i in range(5)]

    '''
    get user profile information, get the notification if the current user same ,
    get the posts for the user, check follow or unfollow depend on the current user and the relations
    '''
    return render(request, 'user_profile/profile.html', {'user_slug': user_slug, 'posts': post_obj, 'total_obj': total_obj, 'notifications': notifications})


'''
we should check if the current user who enter this page same as user
'''

@xframe_options_exempt
def edit_profile(request, user_slug):
    # take the user data from the api
    user_profile_img = None
    user_profile_data = {
        'firstname': 'Qutaiba',
        'lastname': 'Olayyan',
        'age': 22,
        'phone': '0568187266',
        'address': 'Ramallh',
        'status': 'backend developer',
        'about_me': 'like u',
    }
    if request.method == 'POST':
        image_form = PersonalImageForm(request.POST, request.FILES)
        profile_form = ProfileEditForm(request.POST)
        if image_form.is_valid():
            image = request.FILES['image']
            api_image = None

            #fs = FileSystemStorage()

            with image.open('rb') as f:
                api_image = f.read()
                #filename = fs.save(image.name, f)
            f.close()

            '''
            Send image to api
            '''


            #uploaded_file_url = fs.url(filename)


            return HttpResponseRedirect(reverse('user_profile:edit_profile', kwargs={'user_slug': user_slug}))
        if profile_form.is_valid():
            firstname = profile_form.cleaned_data.get('firstname')
            lastname = profile_form.cleaned_data.get('lastname')
            age = profile_form.cleaned_data.get('age')
            phone = profile_form.cleaned_data.get('phone')
            address = profile_form.cleaned_data.get('address')
            status = profile_form.cleaned_data.get('status')
            about_me = profile_form.cleaned_data.get('about_me')
            '''
            send new data by patch to api to update it
            '''
            return HttpResponseRedirect(reverse('user_profile:edit_profile', kwargs={'user_slug': user_slug}))

    else:
        image_form = PersonalImageForm()
        profile_form = ProfileEditForm(initial=user_profile_data)



    return render(request, 'user_profile/edit.html', {'user_slug': user_slug,
                                                      'image_form': image_form,
                                                      'profile_form': profile_form,
                                                      'user_profile_img': user_profile_img,})


def follow(request, related_user_slug):
    if request.method == 'GET':
        print(related_user_slug)
        return HttpResponseRedirect(request.GET.get('next'))
    raise Http404

def unfollow(request, related_user_slug):
    if request.method == 'GET':
        print(related_user_slug)
        return HttpResponseRedirect(request.GET.get('next'))
    raise Http404
