from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL
def create_comment(request, *args, **kwargs):

    headers = {
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    try:
        response = session.post(f'{HOST}/post/comment_create/', headers=headers, data=kwargs['payload'])
    except requests.exceptions.ConnectionError:
        raise Http404

    # should return 201
    return response.status_code