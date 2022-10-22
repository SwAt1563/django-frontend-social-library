from django.core.exceptions import PermissionDenied
from functools import wraps
from django.shortcuts import HttpResponseRedirect, reverse


def is_admin(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        if request.session.has_key('is_admin') and request.session.get('is_admin'):
            return view(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('registration:admin_login'))

    return _view
