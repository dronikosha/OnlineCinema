from django.urls import path
from . import views
from . import consumer

urlpatterns = [
    path('', views.movies, name='home'),
    path('search/', views.search, name='search'),
    path('create_room/<int:movie_id>/', views.create_room, name='create_room'),
    path('room/<str:room_id>/', views.room, name='room'),
    path('video/<str:video_file>/', views.video_view, name='video_view'),
]