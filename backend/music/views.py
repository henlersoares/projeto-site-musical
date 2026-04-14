from rest_framework.viewsets import ModelViewSet
from .models import Artist, Album
from .serializers import ArtistSerializer, AlbumSerializer

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer