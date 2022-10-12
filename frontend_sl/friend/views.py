from django.shortcuts import render
from django.views.generic import ListView
from home.forms import PeopleSearchForm

# Create your views here.


class FollowersListView(ListView):
    template_name = 'friend/friends.html'
    context_object_name = 'objects'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FollowersListView, self).get_context_data(**kwargs)
        context['user_slug'] = 'x'
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
            if self.extra_context.get('people_search'):
                return ['x'] * 50
        return []

class FollowingListView(ListView):
    template_name = 'friend/friends.html'
    context_object_name = 'objects'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FollowingListView, self).get_context_data(**kwargs)
        context['user_slug'] = 'x'
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
            if self.extra_context.get('people_search'):
                return ['x'] * 50
        return []