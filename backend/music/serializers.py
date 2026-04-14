from rest_framework import serializers
from .models import Artist, Album

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist_link.name', read_only=True)

    class Meta:
        model = Album
        fields = '__all__'