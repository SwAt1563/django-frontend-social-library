from django.urls import path, include
from . import views
from registration.permissions import is_authenticated

app_name = 'post'
urlpatterns = [

    path('ps/<slug:post_slug>/', is_authenticated(views.index), name='index'),
    path('edit_post/<slug:post_slug>/', is_authenticated(views.edit_post), name='edit_post'),
    path('create_post/', is_authenticated(views.create_post), name='create_post'),
    path('delete_post/<slug:post_slug>/', is_authenticated(views.delete_post), name='delete_post'),

]

