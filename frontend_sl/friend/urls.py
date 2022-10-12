from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'friend'
urlpatterns = [
    path('followers/<slug:user_related_slug>/', views.FollowersListView.as_view(), name='followers'),
    path('following/<slug:user_related_slug>/', views.FollowingListView.as_view(), name='following'),

]

