from django.contrib import admin
from django.urls import path, include
from . import views
from registration.permissions import is_authenticated
app_name = 'friend'
urlpatterns = [
    path('followers/<slug:user_related_slug>/', is_authenticated(views.FollowersListView.as_view()), name='followers'),
    path('following/<slug:user_related_slug>/', is_authenticated(views.FollowingListView.as_view()), name='following'),

]

