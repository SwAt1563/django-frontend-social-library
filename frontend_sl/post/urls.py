from django.urls import path, include
from . import views

app_name = 'post'
urlpatterns = [

    path('ps/<slug:post_slug>/', views.index, name='index'),
    path('edit_post/<slug:post_slug>/', views.edit_post, name='edit_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete_post/<slug:post_slug>/', views.delete_post, name='delete_post'),

]

