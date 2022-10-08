from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('search/', views.SearchListView.as_view(), name='search'),

]

