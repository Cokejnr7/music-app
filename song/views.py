from django.shortcuts import render
from django.http import FileResponse
from .models import Song,Album,Collection
from .serializers import SongSerializer,AlbumSerializer,CollectionSerializer
from rest_framework import generics
# Create your views here.


# class SongListCreateAPIView(ListCreateAPIView):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer


def home(request):
    songs = Song.objects.all()
    context = {
        'songs': songs
    }
    

    return render(request, 'song/home.html', context)

def collections(request):
    collections = Collection.objects.all()
    context = {
        "collections": collections
    }
    
    return render(request,'song/collections.html',context)



class SongListCreateAPIView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    
class AlbumListCreateAPIView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    
class CollectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    
    
    




