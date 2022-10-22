from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView
from django.http import Http404
from .forms import DashboardSearchForm
from .api.get_admin_posts_api import get_admin_posts
from .api.accept_post_api import accept_post_api
from .api.remove_post_api import remove_post_api

# Create your views here.

def get_posts_status(posts):
    total_posts = len(posts)
    pending_posts = 0
    completed_posts = 0
    for post in posts:
        if post['status'] == 'COMPLETED':
            completed_posts += 1
        elif post['status'] == 'PENDING':
            pending_posts += 1
    status = dict(
        total_posts=total_posts,
        pending_posts=pending_posts,
        completed_posts=completed_posts,
    )
    return status


class DashboardListView(ListView):
    template_name = 'admin_app/dashboard.html'
    context_object_name = 'objects'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
        context['profile_slug'] = self.request.session.get('profile_slug')
        context['is_admin'] = self.request.session.get('is_admin')
        return context

    def get(self, request, *args, **kwargs):
        search_form = DashboardSearchForm(request.GET)

        if search_form.is_valid():
            self.extra_context = {'search_form': search_form,
                                  'search_field': search_form.cleaned_data['search_field']
                                  }
        else:
            self.extra_context = {'search_form': DashboardSearchForm}
        return super(DashboardListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.method == 'GET':
            posts = []
            payload = dict()

            if self.extra_context.get('search_field'):
                payload.update({'filter': self.extra_context.get('search_field')})

            try:

                response_status, data = get_admin_posts(self.request, payload=payload)
            except Http404:
                raise Http404

            if response_status == 200:
                posts = data
                status = get_posts_status(posts)
                self.extra_context.update({'status': status})

            return posts


def add_post(request, post_slug):
    if request.method == 'GET' and request.GET.get('next'):
        try:
            payload = dict(
                user_id=request.session.get('user_id'),
                post_slug=post_slug,
            )
            response_status = accept_post_api(request, payload=payload)
        except Http404:
            return Http404
        return HttpResponseRedirect(request.GET.get('next'))
    return Http404


def delete_post(request, post_slug):
    if request.method == 'GET' and request.GET.get('next'):
        try:
            payload = dict(
                user_id=request.session.get('user_id'),
                post_slug=post_slug,
            )
            response_status = remove_post_api(request, payload=payload)
        except Http404:
            return Http404
        return HttpResponseRedirect(request.GET.get('next'))
    return Http404
