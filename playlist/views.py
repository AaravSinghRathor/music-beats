from django.shortcuts import render, redirect
from .models import Playlist
from beats.models import Beats
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Playlist

# Create your views here.
class PlaylistCreateView(LoginRequiredMixin, CreateView):
    model = Playlist
    template_name = "playlist/create_playlist.html"
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def get_playlists(request):
    playlists = Playlist.objects.filter(user_id=request.user.id)

    return render(request, "playlist/get_playlists.html", {"playlists": playlists})

@login_required
def add_beat_in_playlist(request, playlist_id, beat_id):
    playlist = Playlist.objects.get(id=playlist_id)
    beat = Beats.objects.get(id=beat_id)

    playlist.beats_set.add(beat)
    return HttpResponse("beat added", status=201)

@login_required
def delete_playlist(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    playlist.delete()
    return redirect('get-playlists')

@login_required
def get_playlist(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    beats = playlist.beats_set.all()

    playlists_data = [
        {
            "playlist": playlist,
            "beats": beats
        },
    ]

    context = {
        "playlists_data": playlists_data,
        "have_delete_beat": "true"
    }

    return render(request, "beats/home.html", context)


@login_required
def delete_beat_from_playlist(request, playlist_id, beat_id):

    playlist = Playlist.objects.get(id=playlist_id)
    beat = Beats.objects.get(id=beat_id)
    playlist.beats_set.remove(beat)

    return redirect("get-playlist", playlist_id)