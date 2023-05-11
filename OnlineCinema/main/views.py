from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.conf import settings
import os

from .models import Movie, MovieRoom


def movies(request):
    movies = Movie.objects.all()
    return render(request, 'main/home.html', {'movies': movies})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        movies = Movie.objects.filter(name__icontains=query)
        return render(request, 'main/home.html', {'movies': movies})
    

def create_room(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    room = MovieRoom.objects.create(movie=movie)
    return redirect('room', room.room_id)



def room(request, room_id):
    room = MovieRoom.objects.get(room_id=room_id)
    response = render(request, 'main/room.html', {'room': room})
    response['Accept-Ranges'] = 'bytes'
    print(response.serialize_headers())
    return response



def video_view(request, video_file):
    video_file = video_file.replace('\\', '/')
    file_path = os.path.join(settings.MEDIA_ROOT, video_file)
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="video/mp4")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response