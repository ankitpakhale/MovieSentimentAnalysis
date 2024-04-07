from django.db import models

class MovieReview(models.Model):
    movie_title = models.CharField(max_length=255)
    review_text = models.TextField()
    sentiment = models.CharField(max_length=10)  # Positive or Negative

    def __str__(self):
        return self.movie_title
