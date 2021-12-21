"""
Definition of urls for DjangoSearchView.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from sample import forms, views


urlpatterns = [
    path('admin/', admin.site.urls),
    # Test
    path('', views.AlbumSearchListView.as_view(), name='album'),
    path('musician/', views.MusicianSearchListView.as_view(), name='musician'),

]
