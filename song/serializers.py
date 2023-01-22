from rest_framework import serializers
from .models import Album, Song, Collection, Genre


class GenreSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Genre
        fields = ['name']
        
class SongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True,many=True)
    
    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)

    class Meta:
        model = Collection
        fields = '__all__'

