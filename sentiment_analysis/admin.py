from django.contrib import admin
from .models import MovieReview, SentimentLabel

# Define custom admin classes for MovieReview and SentimentLabel
class MovieReviewAdmin(admin.ModelAdmin):
    # Define fields to be displayed in the admin list view
    list_display = ['movie_title', 'review_text', 'sentiment']

    # Define fields to be searched in the admin
    search_fields = ['movie_title', 'review_text']

class SentimentLabelAdmin(admin.ModelAdmin):
    # Define fields to be displayed in the admin list view
    list_display = ['label_name']

    # Define fields to be searched in the admin
    search_fields = ['label_name']

# Register the models and their custom admin classes
admin.site.register(MovieReview, MovieReviewAdmin)
admin.site.register(SentimentLabel, SentimentLabelAdmin)
