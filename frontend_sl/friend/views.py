from django.shortcuts import render
from django.views.generic import ListView
from home.forms import PeopleSearchForm
from .api.get_followers_api import get_followers_api
from .api.get_following_api import get_following_api
from django.http import Http404
# Create your views here.


class FollowersListView(ListView):
    template_name = 'friend/friends.html'
    context_object_name = 'objects'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FollowersListView, self).get_context_data(**kwargs)
        context['profile_slug'] = self.request.session.get('profile_slug')
        context['is_admin'] = self.request.session.get('is_admin')
        return context

    def get(self, request, *args, **kwargs):
        # extra context that we can use it in template

        people_form = PeopleSearchForm(request.GET)

        if people_form.is_valid():
            self.extra_context = {'people_form': people_form,
                                  'people_search': people_form.cleaned_data['people_search']
                                  }

        else:
            self.extra_context = {
                'people_form': PeopleSearchForm,
            }
        return super(FollowersListView, self).get(request, *args, **kwargs)



    def get_queryset(self):
        if self.request.method == 'GET':
            followers = []
            payload = dict(
                related_user_slug=self.kwargs['user_related_slug'],
                user_id=self.request.session.get('user_id'),
            )

            if self.extra_context.get('people_search'):
                payload.update({'filter': self.extra_context.get('people_search')})

            try:

                response_status, data = get_followers_api(self.request, payload=payload)
            except Http404:
                raise Http404

            if response_status == 200:
                followers = data

            return followers

class FollowingListView(ListView):
    template_name = 'friend/friends.html'
    context_object_name = 'objects'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FollowingListView, self).get_context_data(**kwargs)
        context['profile_slug'] = self.request.session.get('profile_slug')
        context['is_admin'] = self.request.session.get('is_admin')
        return context

    def get(self, request, *args, **kwargs):
        # extra context that we can use it in template

        people_form = PeopleSearchForm(request.GET)

        if people_form.is_valid():
            self.extra_context = {'people_form': people_form,
                                  'people_search': people_form.cleaned_data['people_search']
                                  }

        else:
            self.extra_context = {
                'people_form': PeopleSearchForm,
            }
        return super(FollowingListView, self).get(request, *args, **kwargs)



    def get_queryset(self):
        if self.request.method == 'GET':
            followers = []
            payload = dict(
                related_user_slug=self.kwargs['user_related_slug'],
                user_id=self.request.session.get('user_id'),
            )

            if self.extra_context.get('people_search'):
                payload.update({'filter': self.extra_context.get('people_search')})

            try:

                response_status, data = get_following_api(self.request, payload=payload)
            except Http404:
                raise Http404

            if response_status == 200:
                followers = data

            return followers