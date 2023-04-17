"""
guild_wars_2 URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('guild_wars_2_blog.urls'), name='gw2_urls'),
    path('accounts/', include('allauth.urls')),
]
