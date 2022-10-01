from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import LoginForm, RegisterForm
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            '''
                Save the token in the django session
            '''
            # its save for use HttpResponseRedirect better than render
            # cuz don't let the user when make reverse back to login page
            # to go to post method
            return HttpResponseRedirect(reverse('home:index'))
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'login_form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            question = form.cleaned_data.get('question')
            answer = form.cleaned_data.get('answer')
            '''
                 Create new user by send the information to the api
            '''
            return HttpResponseRedirect(reverse('registration:login'))
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'register_form': form})