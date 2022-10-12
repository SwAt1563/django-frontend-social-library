from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'user_profile'
urlpatterns = [

    path('p/profile/<slug:user_slug>/', views.profile, name='profile'),
    path('p/load_more/<slug:user_slug>/', views.load_more, name='load_more'),
    path('edit/<slug:user_slug>/', views.edit_profile, name='edit_profile'),
    path('f/<slug:related_user_slug>/', views.follow, name='follow'),
    path('unf/<slug:related_user_slug>/', views.unfollow, name='unfollow'),

]

