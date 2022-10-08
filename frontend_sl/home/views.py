from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import PeopleSearchForm, PostSearchForm
from django.views.generic import ListView
from django.http import Http404
# Create your views here.

def index(request):
    user_slug = 'x'
    return render(request, 'home/index.html', {'user_slug': user_slug})


class HomeView(ListView):
    template_name = 'home/index.html'  # redirect template
    context_object_name = 'posts'  # name of posts parameter that we can access in template
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['user_slug'] = 'x'
        return context

    def get(self, request, *args, **kwargs):
        # extra context that we can use it in template
        self.extra_context = {
            'people_search_form': PeopleSearchForm,
            'post_search_form': PostSearchForm,
        }
        return super(HomeView, self).get(request, *args, **kwargs)


    # what we want to put in 'list_objects'
    def get_queryset(self):
        if self.request.method == 'POST':
                return []
        '''
         get files from api
        '''
        return ['x'] * 50


class SearchListView(ListView):
    template_name = 'home/search.html'
    context_object_name = 'objects'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        context['user_slug'] = 'x'
        return context

    def get(self, request, *args, **kwargs):
        # extra context that we can use it in template
        print(self.request.GET)
        self.extra_context = {
            'people_form': PeopleSearchForm,
            'post_form': PostSearchForm,
        }
        return super(SearchListView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        people_form = PeopleSearchForm(request.POST)
        post_form = PostSearchForm(request.POST)

        if people_form.is_valid():

            self.extra_context = {'people_form': people_form,
                                  'post_form': PostSearchForm}

            self.request.session.update({'people_search': people_form.cleaned_data['people_search']})

            self.request.session.pop('post_search', None)


        elif post_form.is_valid():

            self.extra_context = {'people_form': PeopleSearchForm,
                                  'post_form': post_form}

            self.request.session.update({'post_search': post_form.cleaned_data['post_search']})

            self.request.session.pop('people_search', None)

        return super(SearchListView, self).get(request, *args, **kwargs)


    def get_queryset(self):

        if self.request.session.get('post_search'):
            self.extra_context.update({'post_template': True})
            return ['x'] * 50
        elif self.request.session.get('people_search'):
            self.extra_context.update({'people_template': True})
            return ['x'] * 50
        return []

