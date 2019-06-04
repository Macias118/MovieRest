from rest_framework import serializers
from .models import Movie
from .models import Comment
import requests


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'comments', 'details')

    def create(self, data):
        api_url = 'http://www.omdbapi.com/?apikey=860f6403&t=' + data['title']
        r = requests.get(url=api_url)
        if r.json()['Response'] == 'False':
            return serializers.ValidationError({'message': r.details['Error']})
        return Movie.objects.create(comments=[], details=r.json())


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id', 'comment_text')

    def create(self, data):
        movie = Movie.objects.filter(pk=data['movie_id'])
        print('movie object => {}'.format(movie))
        return Comment.objects.create(comment_text=data['comment_text'])