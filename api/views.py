import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie


class MovieView(APIView):
    def post(self, request, format=None):
        movie_title = request.POST['title']
        empty = {'result': 'succcess'}
        Movie(total_comments=2, rank=34, details='det').save()
        # send request to api
        api_url = 'http://www.omdbapi.com/?apikey=860f6403&t=' + movie_title
        r = requests.get(url=api_url)
        print(r.json()) 
        return Response(empty, status=status.HTTP_201_CREATED)

    def get(self, request):
        m = Movie.objects.all()
        print(m)
        return Response({'great': 'awesome get'}, status=status.HTTP_200_OK)

# class SurveyAPIView(APIView):

#     def post(self, request, format=None):
#         serializer = SurveySerializer(request.data)
#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# and in urls.py add a new line like:

