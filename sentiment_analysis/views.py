# sentiment_analysis/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MovieReview
import random
from .utils import load_sentiment_model
from .forms import MovieReviewForm
from .constents import MOVIE_TITLES, RESPONSES, MODEL_PATH
import subprocess



def train_model(request):
    if request.method == 'POST':
        # Run the train_model.py script using subprocess
        process = subprocess.Popen(['python', 'sentiment_analysis/train_model.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            # Script executed successfully
            return HttpResponse('Model training completed successfully!')
        else:
            # Script encountered an error
            return HttpResponse(f'Error occurred during model training: {stderr.decode()}')
    else:
        return render(request, 'train_model.html')
    

def submit_review(request):
    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            movie_title = form.cleaned_data['movie_title']
            review_text = form.cleaned_data['review_text']
            

        # Check if the user wants to add random movie data
        if 'add_random_data' in request.POST:
            count = int(request.POST.get('random_data_count', 1))
            generate_random_movie_data(count)

        # Check if the user wants to manipulate movie data
        if 'manipulate_data' in request.POST:
            action = request.POST.get('manipulate_action')
            count = int(request.POST.get('manipulate_count', 1))
            if action == 'add':
                generate_random_movie_data(count)
            elif action == 'delete':
                delete_added_movie_data(count)

            # Load the sentiment analysis model
            sentiment_model = load_sentiment_model(MODEL_PATH)
            
            # Classify the sentiment of the review using the loaded model
            sentiment = sentiment_model.predict([review_text])[0]
            
            # Save the submitted review to the database
            MovieReview.objects.create(movie_title=movie_title, review_text=review_text, sentiment=sentiment)
            
            return HttpResponse('Review submitted successfully!')
    else:
        form = MovieReviewForm()
    return render(request, 'submit_review.html', {'form': form})


def view_reviews(request):
    reviews = MovieReview.objects.all()
    return render(request, 'view_reviews.html', {'reviews': reviews})


def delete_added_movie_data(count):
    added_movies = MovieReview.objects.filter(movie_title__in=MOVIE_TITLES)[:count]
    for movie in added_movies:
        movie.delete()
    print("*"*50)
    print(f"Deleted {count} added movie reviews.")
    print("*"*50)



def generate_random_movie_data(num_movies):
    for _ in range(num_movies):
        movie_title = random.choice(MOVIE_TITLES)
        review_text = random.choice(RESPONSES)

        movie_review = MovieReview.objects.create(
            movie_title=movie_title,
            review_text=review_text,
        )
        print("*"*50)
        print(f"Created review for {movie_title}")
        print("*"*50)



def manipulate_movie_data(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            count = int(request.POST.get('count', 1))
            generate_random_movie_data(count)
            return HttpResponse(f'Added {count} random movie reviews successfully!')
        elif action == 'delete':
            count = int(request.POST.get('count', 1))
            delete_added_movie_data(count)
            return HttpResponse(f'Deleted {count} added movie reviews successfully!')
        else:
            return HttpResponse('Invalid action.')
    else:
        return render(request, 'manipulate_movie_data.html')
    






