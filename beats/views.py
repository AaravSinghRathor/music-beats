from django.shortcuts import render
from .models import Beats
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

def home(request):
    beats = Beats.objects.all()
    return render(request, "beats/home.html", {'beats': beats})

class BeatsCreateView(LoginRequiredMixin, CreateView):
    model = Beats
    template_name = "beats/create_beats.html"
    fields = ['singer', 'title', 'coverpage', 'audio']
    success_url = reverse_lazy('home')

def play_beat(request, id):
    beat = Beats.objects.get(id=id)
    return render(request, "beats/play_beat.html", {'beat': beat})
