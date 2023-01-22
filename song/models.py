from django.db import models
from django.contrib.auth.models import User
from .helpers import get_duration
# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.ImageField()
    description = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.ImageField(blank=True)
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=True, blank=True)
    featuring = models.CharField(max_length=150,blank=True,null=True)
    audio_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genre = models.ManyToManyField("Genre")
    

    def __str__(self) -> str:
        return self.title

    @property
    def duration(self):
        return get_duration(self.audio_file)
    
    def save(self, *args, **kwargs):
        if not(self.cover_image) and self.album:
            self.cover_image = self.album.cover_image
        return super().save(*args,**kwargs)
        


class Collection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="collections")
    title = models.CharField(max_length=50)
    song = models.ManyToManyField(Song)
    cover_image = models.ImageField()

    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name


class Like(models.Model):
    song = models.ForeignKey(to=Song,on_delete=models.PROTECT,related_name="likes")
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="favorite")
    
    class Meta:
        unique_together = ['song','owner']