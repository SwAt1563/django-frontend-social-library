"""frontend_sl URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('admin/', admin.site.urls),
    path('au/', include('registration.urls', namespace='registration')),
    path('profile/', include('user_profile.urls', namespace='user_profile')),
    path('post/', include('post.urls', namespace='post')),

]

# for confirm the static paths
# just for development stage
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)