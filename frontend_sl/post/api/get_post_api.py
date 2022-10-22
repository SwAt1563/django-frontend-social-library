from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL
def get_post(request, post_slug, *args, **kwargs):
    headers = {
        'Authorization': f'Bearer {str(request.session.get("access"))}',
    }
    try:
        response = session.get(f'{HOST}/post/post_review/{post_slug}/', headers=headers)
    except requests.exceptions.ConnectionError:
        raise Http404

    data = None

    if response.status_code == 200:
        data = json.loads(response.content)

    # should return 200
    return response.status_code, data