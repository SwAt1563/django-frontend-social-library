from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView
from django.http import Http404
from .forms import DashboardSearchForm
# Create your views here.


class DashboardListView(ListView):
    template_name = 'admin_app/dashboard.html'
    context_object_name = 'objects'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
        context['user_slug'] = 'x'
        context['this_post_slug'] = 'x'
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
            if self.extra_context.get('search_field'):
                '''
                    use api to search by file title and user name
                '''
                return ['x'] * 50
            else:
                # return all posts
                return ['x'] * 50
        return []


def add_post(request, post_slug):
    if request.method == 'GET' and request.GET.get('next'):
        'use api to add post'
        return HttpResponseRedirect(request.GET.get('next'))
    return Http404

def delete_post(request, post_slug):

    if request.method == 'GET' and request.GET.get('next'):
        'use api to delete post'
        return HttpResponseRedirect(request.GET.get('next'))
    return Http404