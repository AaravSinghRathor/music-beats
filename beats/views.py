from django.shortcuts import render, redirect
from .models import Beats, LikedBeats
from playlist.models import Playlist
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

def home(request):
    trending_playlist = Playlist.objects.get(name="Trending Beats")
    trending_beats = trending_playlist.beats_set.all()

    playlists_data = [
        {
            "playlist": trending_playlist,
            "beats": trending_beats
        },
        {
            "playlist": trending_playlist,
            "beats": trending_beats
        },
    ]

    if request.user.is_authenticated:
        context = {
            "playlists_data": playlists_data,
            "user_playlists": Playlist.objects.filter(user_id=request.user.id)
        }
    else:
        context = {
            "playlists_data": playlists_data
        }

    return render(request, "beats/home.html", context)

class BeatsCreateView(LoginRequiredMixin, CreateView):
    model = Beats
    template_name = "beats/create_beats.html"
    fields = ['singer', 'title', 'coverpage', 'audio']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def play_beat(request, id):
    beat = Beats.objects.get(id=id)
    return render(request, "beats/play_beat.html", {'beat': beat})

@login_required
def liked_beats(request):
    liked_beats = [object.beat for object in LikedBeats.objects.filter(user_id=request.user.id)]

    playlists_data = [
        {
            "playlist_name": 'Liked Beats',
            "beats": liked_beats
        },
    ]
    return render(request, "beats/home.html", {'playlists_data': playlists_data})

@login_required
def like_beat(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
    beat = Beats.objects.get(id=id)
    if not beat:
        return HttpResponseNotFound("Beat not found")

    liked_beat = LikedBeats(user=user, beat=beat)
    liked_beat.save()
    return HttpResponse(content="<p>Beat added successfully</p>", status=201)

@login_required
def dislike_beat(request, id):
    beat = Beats.objects.get(id=id)
    if not beat:
        return HttpResponseNotFound("Beat not found")

    liked_beat = LikedBeats.objects.get(user_id=request.user.id, beat=beat)
    liked_beat.delete()
    return HttpResponse(content="<p>Beat removed successfully</p>", status=200)

@login_required
def check_is_liked_beat(request, id):
    beat = Beats.objects.get(id=id)
    if not beat:
        return HttpResponseNotFound("Beat not found")

    liked_beats_record = LikedBeats.objects.filter(
        user_id=request.user.id,
        beat=beat
    )
    if liked_beats_record.exists():
        return HttpResponse(content="Beat found in liked playlist", status=200)
    else:
        return HttpResponseNotFound("Beat does not exist in liked playlist")

@login_required
def delete_beat(request, beat_id):

    beat = Beats.objects.get(id=beat_id)
    beat.delete()

    return redirect("home")