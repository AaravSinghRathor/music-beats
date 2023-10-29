from django.contrib import admin
from .models import Beats, LikedBeats

# Register your models here.
admin.site.register(Beats)
admin.site.register(LikedBeats)