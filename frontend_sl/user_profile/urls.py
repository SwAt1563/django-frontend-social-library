from django.contrib import admin
from django.urls import path, include
from . import views
from registration.permissions import is_authenticated

app_name = 'user_profile'
urlpatterns = [

    path('p/profile/<slug:profile_slug>/', is_authenticated(views.profile), name='profile'),
    path('p/load_more/<slug:profile_slug>/', is_authenticated(views.load_more), name='load_more'),
    path('edit/<slug:profile_slug>/', is_authenticated(views.edit_profile), name='edit_profile'),
    path('f/<slug:related_profile_slug>/', is_authenticated(views.follow), name='follow'),
    path('unf/<slug:related_profile_slug>/', is_authenticated(views.unfollow), name='unfollow'),

]

