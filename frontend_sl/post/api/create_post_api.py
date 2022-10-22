from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL


def create_post_api(request, *args, **kwargs):

    headers = {
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    try:
        files = {'file': kwargs['payload']['file']}

        response = session.post(f'{HOST}/post/post_create/', headers=headers, data=kwargs['payload'],
                                files=files)
    except requests.exceptions.ConnectionError:
        raise Http404

    # should return 201
    return response.status_code