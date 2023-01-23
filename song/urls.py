from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('playlist',views.collections,name="playlist"),
    path('songs', views.SongListCreateAPIView.as_view()),
    path('albums', views.AlbumListCreateAPIView.as_view()),
    path('collections', views.CollectionListCreateAPIView.as_view()),
]
