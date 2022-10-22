from django.contrib import admin
from django.urls import path, include
from . import views
from registration.permissions import is_authenticated
from .permissions import is_admin

app_name = 'admin_app'
urlpatterns = [

    path('', is_admin(is_authenticated(views.DashboardListView.as_view())), name='dashboard'),
    path('add_post/<slug:post_slug>/', is_admin(is_authenticated(views.add_post)), name='add_post'),
    path('delete_post/<slug:post_slug>/', is_admin(is_authenticated(views.delete_post)), name='delete_post'),
]

