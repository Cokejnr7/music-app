from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.ImageField()
    description = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.ImageField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    audio_file = models.FileField()

    def __str__(self) -> str:
        return self.title

    @property
    def duration(self):
        return self


class Collection(models.Model):
    title = models.CharField(max_length=50)
    song = models.ManyToManyField(Song)
    cover_image = models.ImageField()

    def __str__(self) -> str:
        return self.title
