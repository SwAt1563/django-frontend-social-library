from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'admin_app'
urlpatterns = [

    path('', views.DashboardListView.as_view(), name='dashboard'),
    path('add_post/<slug:post_slug>/', views.add_post, name='add_post'),
    path('delete_post/<slug:post_slug>/', views.delete_post, name='delete_post'),
]

