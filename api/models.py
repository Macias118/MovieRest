from django.db import models

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    total_comments = models.IntegerField()
    rank = models.IntegerField()
    details = models.TextField()

    def __repr__(self):
        return str({
            'id': self.movie_id,
            'rank': self.rank,
            'total_comments': self.total_comments,
            'details': self.details})
