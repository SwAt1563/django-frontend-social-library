from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import PeopleSearchForm, PostSearchForm
from django.views.generic import ListView
from django.http import Http404
from .api.home_api import get_all_posts, get_top_users
from .api.search_api import search_posts, search_users

# Create your views here.


class HomeView(ListView):
    template_name = 'home/index.html'  # redirect template
    context_object_name = 'posts'  # name of posts parameter that we can access in template
    paginate_by = 4


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['profile_slug'] = self.request.session.get('profile_slug')
        context['is_admin'] = self.request.session.get('is_admin')
        return context

    def get(self, request, *args, **kwargs):
        # extra context that we can use it in template
        self.extra_context = {
            'people_search_form': PeopleSearchForm,
            'post_search_form': PostSearchForm,
        }

        try:
            response_status, data = get_top_users(self.request)
        except Http404:
            raise Http404

        if response_status == 200:
            self.extra_context.update({'top_users': data})

        return super(HomeView, self).get(request, *args, **kwargs)


    def get_queryset(self):
        if self.request.method == 'GET':

            try:
                response_status, data = get_all_posts(self.request)
            except Http404:
                raise Http404

            if response_status == 200:
                return data

            return []


class SearchListView(ListView):
    template_name = 'home/search.html'
    context_object_name = 'objects'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        context['profile_slug'] = self.request.session.get('profile_slug')
        context['is_admin'] = self.request.session.get('is_admin')
        return context

    def get(self, request, *args, **kwargs):
        # extra context that we can use it in template

        people_form = PeopleSearchForm(request.GET)
        post_form = PostSearchForm(request.GET)

        if people_form.is_valid():

            self.extra_context = {'people_form': people_form,
                                  'post_form': PostSearchForm,
                                  'people_search': people_form.cleaned_data['people_search']
                                  }



        elif post_form.is_valid():
            self.extra_context = {'people_form': PeopleSearchForm,
                                  'post_form': post_form,
                                  'post_search': post_form.cleaned_data['post_search']}

        else:
            self.extra_context = {
                'people_form': PeopleSearchForm,
                'post_form': PostSearchForm,
            }
        return super(SearchListView, self).get(request, *args, **kwargs)



    def get_queryset(self):
        if self.request.method == 'GET':
            if self.extra_context.get('post_search'):
                self.extra_context.update({'post_template': True})

                payload = dict(
                    filter=self.extra_context.get('post_search'),
                )
                try:
                    response_status, data = search_posts(self.request, payload=payload)
                except Http404:
                    raise Http404

                if response_status == 200:
                    return data

                return []
            elif self.extra_context.get('people_search'):
                self.extra_context.update({'people_template': True})
                payload = dict(
                    filter=self.extra_context.get('people_search'),
                    user_id=self.request.session.get('user_id'),
                )
                try:
                    response_status, data = search_users(self.request, payload=payload)
                except Http404:
                    raise Http404

                if response_status == 200:
                    return data

                return []
            return []

