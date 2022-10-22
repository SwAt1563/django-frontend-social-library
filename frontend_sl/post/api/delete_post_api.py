from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL
def delete_post_api(request, post_slug, *args, **kwargs):
    headers = {
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    try:
        response = session.delete(f'{HOST}/post/post_delete/{post_slug}/', headers=headers, data=kwargs['payload'])
    except requests.exceptions.ConnectionError:
        raise Http404

    # should return 204
    return response.status_code