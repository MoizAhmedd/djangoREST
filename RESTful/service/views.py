from django.shortcuts import render
from .models import Songs
from .serializers import SongsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class SongsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Songs.objects.get(pk=pk)
        except Songs.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        songs = self.get_object(pk)
        serializer = SongsSerializer(songs)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        songs = self.get_object(pk)
        serializer = SongsSerializer(songs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        songs = self.get_object(pk)
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)