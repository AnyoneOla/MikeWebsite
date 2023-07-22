#-*- coding:utf-8 -*-

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# namespace
app_name = 'it_works'

urlpatterns = [
    # Create a task
    path('', views.index, name='index'),
    path('requested_songs/', views.requested_songs, name='requested_songs'),
    path('songRequest/', views.songRequest, name='songRequest'),
    path('addSongsPage/', views.addSongsPage, name='addSongsPage'),
    path('addSongs/', views.addSongs, name='addSongs'),
    path('clearListPage/', views.clearListPage, name='clearListPage'),
    path('clearList/', views.clearList, name='clearList'),
    path('searchSong/', views.searchSong, name='searchSong'),
]

urlpatterns += staticfiles_urlpatterns()