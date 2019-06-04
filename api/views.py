import requests
from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer
import json


class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        print('serializer => {}\n {}'. format(serializer, self.request.data['title']))
        # title = serializer
        serializer.save(title=self.request.data['title'])

