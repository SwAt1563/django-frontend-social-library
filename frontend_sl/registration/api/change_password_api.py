from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL

def get_reset_password_token(request, *args, **kwargs):
    try:
        response = session.post(f'{HOST}/account/reset_password_token/', kwargs['payload'])
    except requests.exceptions.ConnectionError:
        raise Http404

    if response.status_code == 200:
        data = json.loads(response.content)
        request.session.update(data)

    return response.status_code

def change_new_password(*args, **kwargs):
    try:
        response = session.post(f'{HOST}/account/change_password/', kwargs['payload'])
    except requests.exceptions.ConnectionError:
        raise Http404

    return response.status_code
