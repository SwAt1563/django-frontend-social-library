from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'registration'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('register/', views.register, name='register'),
    path('reset_email/', views.reset_password_email, name='reset_email'),
    path('reset_password/<int:pk>/', views.reset_password_form, name='reset_password'),
    path('reset_done/', views.reset_password_done, name='reset_done'),
    path('logout/', views.logout, name='logout'),

]

