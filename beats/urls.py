from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.BeatsCreateView.as_view(), name="create-beats"),
    path("play/<int:id>", views.play_beat, name="play-beat")
]
