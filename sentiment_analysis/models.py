from django.db import models

# sentiment_analysis/models.py
from django.db import models

class MovieReview(models.Model):
    movie_title = models.CharField(max_length=255)
    review_text = models.TextField()
    sentiment = models.CharField(max_length=10)  # Positive or Negative

    def __str__(self):
        return self.movie_title

class SentimentLabel(models.Model):
    label_name = models.CharField(max_length=20)

    def __str__(self):
        return self.label_name
