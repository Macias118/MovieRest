from rest_framework import serializers
from .models import Movie
import requests

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'rank', 'total_comments', 'details')
        read_only_fields = ('movie_id', 'rank', 'total_comments', 'details')

    def create(self, data):
        api_url = 'http://www.omdbapi.com/?apikey=860f6403&t=' + data['title']
        r = requests.get(url=api_url)
        if r.json()['Response'] == 'False':
            return serializers.ValidationError({'message': r.details['Error']})
        return Movie.objects.create(total_comments=1, rank=1, details=r.json())