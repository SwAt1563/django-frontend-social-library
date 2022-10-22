from django.core.exceptions import PermissionDenied
from functools import wraps
from django.shortcuts import HttpResponseRedirect, reverse
from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL
def check_token_expired(request, *args, **kwargs):

    try:
        response = session.post(f'{HOST}/account/check_token/', kwargs['payload'])
    except requests.exceptions.ConnectionError:
        raise Http404

    # token not expired yet
    if response.status_code == 200:
        data = json.loads(response.content)
        request.session['access'] = data['access']
        return True

    return False



def is_authenticated(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.session.has_key('access') and request.session.has_key('refresh') and request.session.has_key(
                'username') and request.session.has_key('email') and request.session.has_key('user_id') and request.session.has_key(
                'profile_slug') and request.session.has_key('is_admin'):

            payload = dict(access=request.session.get('access'), refresh=request.session.get('refresh'))
            if check_token_expired(request, payload=payload):
                return view(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(reverse('registration:logout'))
        return HttpResponseRedirect(reverse('registration:login'))

    return _view
