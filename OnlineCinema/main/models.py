from django.db import models
import uuid

class Movie(models.Model):
    name = models.CharField(max_length=100)
    src = models.CharField(max_length=100)
    
    
class MovieRoom(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room_id = models.UUIDField(default=uuid.uuid4, editable=False)