"""
Definition of urls for DjangoSearchView.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from sample import forms, views


urlpatterns = [
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    # Test
    path('', views.AlbumSearchListView.as_view(), name='album'),
    path('musician/', views.MusicianSearchListView.as_view(), name='musician'),

]
