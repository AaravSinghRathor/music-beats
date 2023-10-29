from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.BeatsCreateView.as_view(), name="create-beats"),
    path("delete/<int:beat_id>", views.delete_beat, name="delete-beat"),
    path("play/<int:id>", views.play_beat, name="play-beat"),
    path("like/<int:id>", views.like_beat, name="like-beat"),
    path("dislike/<int:id>", views.dislike_beat, name="dislike-beat"),
    path("liked-beats/", views.liked_beats, name="liked-beats"),
    path("check-liked-beat/<int:id>", views.check_is_liked_beat, name="check-liked-beat"),
]
