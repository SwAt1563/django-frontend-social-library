from django.contrib import admin
from django.urls import path, include
from . import views
from registration.permissions import is_authenticated

app_name = 'home'

urlpatterns = [

    path('', is_authenticated(views.HomeView.as_view()), name='index'),
    path('search/', is_authenticated(views.SearchListView.as_view()), name='search'),

]

