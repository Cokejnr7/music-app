from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('web-collections',views.collections),
    path('songs', views.SongListCreateAPIView.as_view()),
    path('albums', views.AlbumListCreateAPIView.as_view()),
    path('collections', views.CollectionListCreateAPIView.as_view()),
]
