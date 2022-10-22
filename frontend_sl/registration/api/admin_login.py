from frontend_sl.api import session
import requests
from django.conf import settings
from django.urls.exceptions import Http404
import json

HOST = settings.API_URL
def admin_login_api(request, *args, **kwargs):

    try:
        response = session.post(f'{HOST}/account/token/', kwargs['payload'])
    except requests.exceptions.ConnectionError:
        raise Http404

    if response.status_code == 200:
        data = json.loads(response.content)
        request.session.update(data)

    return response.status_code
