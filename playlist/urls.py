from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.PlaylistCreateView.as_view(), name="create-playlist"),
    path("", views.get_playlists, name="get-playlists"),
    path("delete/<int:playlist_id>", views.delete_playlist, name="delete-playlist"),
    path("<int:playlist_id>/delete/<int:beat_id>", views.delete_beat_from_playlist, name="delete-beat-from-playlist"),
    path("<int:playlist_id>/add/<int:beat_id>/", views.add_beat_in_playlist, name="add-beat-in-playlist"),
    path("<int:playlist_id>/", views.get_playlist, name="get-playlist"),
]
