from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL



def remove_post_api(request, *args, **kwargs):
    headers = {
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    try:
        response = session.delete(f'{HOST}/admin_app/remove_post/', headers=headers, data=kwargs['payload'])
    except requests.exceptions.ConnectionError:
        raise Http404

    # should return 204
    return response.status_code


