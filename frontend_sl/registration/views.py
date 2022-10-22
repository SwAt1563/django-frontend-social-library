from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import LoginForm, RegisterForm, ResetPasswordForm, ResetEmailForm, AdminLoginForm
from datetime import timedelta, datetime
from django.http import Http404
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.dateparse import parse_date
from .api.register import registration
from .api.user_login import user_login
from .api.admin_login import admin_login_api
from .api.change_password_api import get_reset_password_token, change_new_password

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            payload = dict(
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password')
            )

            try:
                response_status = user_login(request, payload=payload)
            except Http404:
                return Http404
            if response_status == 200:
                # its save for use HttpResponseRedirect better than render
                # cuz don't let the user when make reverse back to login page
                # to go to post method
                return HttpResponseRedirect(reverse('home:index'))
            else:
                return HttpResponseRedirect(reverse('registration:login'))

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'login_form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            payload = dict(
                email=form.cleaned_data.get('email'),
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                password2=form.cleaned_data.get('password2'),
                question=form.cleaned_data.get('question'),
                answer=form.cleaned_data.get('answer'),
            )
            try:
                response_status = registration(payload=payload)
            except Http404:
                return Http404
            if response_status == 201:
                return HttpResponseRedirect(reverse('registration:login'))
            else:
                # or you can raise errors depend on the response_status
                return Http404
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'register_form': form})


def reset_password_email(request):
    if request.method == 'POST':
        form = ResetEmailForm(request.POST)
        if form.is_valid():
            payload = dict(
                email=form.cleaned_data.get('email'),
                question=form.cleaned_data.get('question'),
                answer=form.cleaned_data.get('answer'),
            )

            try:
                response_status = get_reset_password_token(request, payload=payload)
            except Http404:
                return Http404

            if response_status == 200:
                slug = request.session.get('reset_password_token')

                # for just let this user update his password in 30m
                time_now = datetime.now()
                key = str(slug) + '_reset_password'
                date_to_string = json.dumps(
                    {key: time_now},
                    sort_keys=True,
                    indent=1,
                    cls=DjangoJSONEncoder
                )
                json_to_dic = json.loads(date_to_string)
                request.session.update(json_to_dic)
                return HttpResponseRedirect(reverse('registration:reset_password', kwargs={'slug': slug}))
            else:
                form.errors['email'] = 'Please write the correct answer on the exists email'

    else:
        form = ResetEmailForm
    return render(request, 'registration/reset_password_email.html', {'reset_form': form})


def reset_password_form(request, slug):
    def convert_string_to_date(date):
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
        return date

    key = str(slug) + '_reset_password'
    if not request.session.get(key):
        raise Http404
    else:
        old_time = request.session.get(key)
        old_time = convert_string_to_date(old_time)
        current_time = datetime.now()

        # just 30m for user to update his password
        if current_time - old_time > timedelta(minutes=30):
            del request.session[key]
            if request.session.get('reset_password_token'):
                del request.session['reset_password_token']
            raise Http404

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('password')

            payload = dict(
                reset_password_token=request.session.get('reset_password_token'),
                new_password=new_password,
            )

            try:
                response_status = change_new_password(payload=payload)
            except Http404:
                return Http404

            if response_status == 200:
                # delete the key in the session after update new password
                if request.session.get(key):
                    del request.session[key]
                if request.session.get('reset_password_token'):
                    del request.session['reset_password_token']
                return HttpResponseRedirect(reverse('registration:reset_done'))
            else:
                form.errors['password'] = 'Not strong password'
    else:
        form = ResetPasswordForm
    return render(request, 'registration/reset_password_form.html', {'reset_password': form})


def reset_password_done(request):
    return render(request, 'registration/reset_password_done.html')


def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('registration:login'))


def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            payload = dict(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            try:
                response_status = admin_login_api(request, payload=payload)
            except Http404:
                return Http404
            if response_status == 200:
                # its save for use HttpResponseRedirect better than render
                # cuz don't let the user when make reverse back to login page
                # to go to post method
                return HttpResponseRedirect(reverse('admin_app:dashboard'))
            else:
                return HttpResponseRedirect(reverse('registration:admin_login'))


    else:
        form = AdminLoginForm()
    return render(request, 'registration/admin_login.html', {'login_form': form})
