from django.db import models

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_text = models.TextField()

    def __repr__(self):
        return str({
            'comment_id': self.comment_id,
            'comment_text': self.comment_text})


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    comments = models.ManyToManyField(Comment)
    details = models.TextField()

    def __repr__(self):
        return str({
            'id': self.movie_id,
            'comments': self.comments,
            'details': self.details})
