from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import LoginForm, RegisterForm, ResetPasswordForm, ResetEmailForm, AdminLoginForm
from datetime import datetime, timedelta
from django.http import Http404
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.dateparse import parse_date

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


def reset_password_email(request):
    if request.method == 'POST':
        form = ResetEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            question = form.cleaned_data.get('question')
            answer = form.cleaned_data.get('answer')
            pk = 0
            '''
             get the pk of the user from the api if the email is exist 
             and the question and answer is correct
            '''

            # for just let this user update his password in 5m
            time_now = datetime.now()
            key = str(pk) + '_reset_password'
            date_to_string = json.dumps(
                {key: time_now},
                sort_keys=True,
                indent=1,
                cls=DjangoJSONEncoder
            )
            json_to_dic = json.loads(date_to_string)
            request.session.update(json_to_dic)

            return HttpResponseRedirect(reverse('registration:reset_password', kwargs={'pk': pk}))
    else:
        form = ResetEmailForm
    return render(request, 'registration/reset_password_email.html', {'reset_form': form})


def reset_password_form(request, pk):
    def convert_string_to_date(date):
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
        return date

    key = str(pk) + '_reset_password'
    if not request.session.get(key):
        raise Http404
    else:
        old_time = request.session.get(key)
        old_time = convert_string_to_date(old_time)
        current_time = datetime.now()

        # just 5m for user to update his password
        if current_time - old_time > timedelta(minutes=5):
            request.session.delete(key)
            raise Http404

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data.get('password')
            pass2 = form.cleaned_data.get('password2')
            '''
             use the api for send the new password to the (pk) user
            '''

            # delete the key in the session after update new password
            request.session.delete(key)

            return HttpResponseRedirect(reverse('registration:reset_done'))
    else:
        form = ResetPasswordForm
    return render(request, 'registration/reset_password_form.html', {'reset_password': form})


def reset_password_done(request):
    return render(request, 'registration/reset_password_done.html')


def logout(request):
    return HttpResponseRedirect(reverse('registration:login'))



def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            '''
                Save the token in the django session
            '''
            # its save for use HttpResponseRedirect better than render
            # cuz don't let the user when make reverse back to login page
            # to go to post method
            return HttpResponseRedirect(reverse('admin_app:dashboard'))
    else:
        form = AdminLoginForm()
    return render(request, 'registration/admin_login.html', {'login_form': form})