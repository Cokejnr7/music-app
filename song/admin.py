from django.contrib import admin
from .models import Album, Song, Collection, Genre,Like
# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Collection)
admin.site.register(Genre)
admin.site.register(Like)
