from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL
def update_profile_image(request, profile_slug, *args, **kwargs):
    headers = {
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    try:
        files = {'image': kwargs['payload']['image']}
        response = session.put(f'{HOST}/profile/p/{profile_slug}/', headers=headers, data=kwargs['payload'], files=files)
    except requests.exceptions.ConnectionError:
        raise Http404


    # should return 200
    return response.status_code


def update_profile(request, profile_slug, *args, **kwargs):
    headers = {
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    try:
        response = session.put(f'{HOST}/profile/p/{profile_slug}/', headers=headers, data=kwargs['payload'])
    except requests.exceptions.ConnectionError:
        raise Http404

    # should return 200
    return response.status_code