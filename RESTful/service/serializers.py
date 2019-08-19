from rest_framework import serializers
from .models import Songs 

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs 
        fields = ['id','song','artist']
"""
class SongsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    song = serializers.TextField()
    artist = serializers.TextField()

    def create(self,validated_data):
        return Songs.object.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.song = validated_data.get('song', instance.song)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.save()
        return instance
"""