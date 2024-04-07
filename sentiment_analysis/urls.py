from django.urls import path
from . import views

urlpatterns = [
    path('submit-review/', views.submit_review, name='submit_review'),
    path('view-reviews/', views.view_reviews, name='view_reviews'),
    path('manipulate-data/', views.manipulate_movie_data, name='manipulate_movie_data'),
    # path('train_model/', views.train_model, name='train_model'),
]
