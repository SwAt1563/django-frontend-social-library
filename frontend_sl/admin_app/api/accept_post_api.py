from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL

def accept_post_api(request, *args, **kwargs):

    headers = {
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    try:
        response = session.post(f'{HOST}/admin_app/accept_post/', headers=headers, data=kwargs['payload'])
    except requests.exceptions.ConnectionError:
        raise Http404

    # should return 201
    return response.status_code



