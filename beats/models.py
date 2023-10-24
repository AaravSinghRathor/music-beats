from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone

class Playlist(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Beats(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True, blank=True)
    singer = models.CharField(max_length=100, default='None')
    title = models.CharField(max_length=100)
    coverpage = models.FileField(upload_to='beats/images')
    audio = models.FileField(upload_to="beats/audio")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
