from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MovieReview
from .forms import MovieReviewForm
from .utils import load_sentiment_model, classify_sentiment, preprocess_review
from .constants import MOVIE_TITLES, RESPONSES, MODEL_PATH
from sklearn.feature_extraction.text import TfidfVectorizer
from django.contrib import messages
import random
import subprocess


# Initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()


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


def save_review_to_database(movie_title, review_text):
    # Load sentiment model
    sentiment_model = load_sentiment_model(MODEL_PATH)
    
    # Classify sentiment of the review
    sentiment = classify_sentiment(sentiment_model, review_text)
    
    # Save the review to the database with the predicted sentiment
    movie_obj = MovieReview.objects.create(movie_title=movie_title, review_text=review_text, sentiment=sentiment)
    print("\n\n" + "*" * 100)
    print(f'➡ movie_title: {movie_obj}')
    print(f'➡ movie_obj: {sentiment}')
    print("*" * 100 + "\n\n")


def submit_review(request):
    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            # Get the review text and movie title from the form
            review_text = form.cleaned_data['review_text']
            movie_title = form.cleaned_data['movie_title']
            
            # Save the review to the database
            save_review_to_database(movie_title, review_text)
            
            # Set success message in session
            messages.success(request, 'Data saved successfully.')
            
            # Redirect to the same page to prevent form resubmission
            return redirect('submit_review')
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
    print("\n\n" + "*" * 100)
    print(f"Deleted {count} movie reviews.")
    print("*" * 100 + "\n\n")

    

def generate_random_movie_data(num_movies):
    for _ in range(num_movies):
        movie_title = random.choice(MOVIE_TITLES)
        review_text = random.choice(RESPONSES)

        save_review_to_database(movie_title, review_text)


def manipulate_movie_data(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            count = int(request.POST.get('count', 1))
            generate_random_movie_data(count)
            messages.success(request, f'Added {count} random movie reviews successfully!')

        elif action == 'delete':
            count = int(request.POST.get('count', 1))
            delete_added_movie_data(count)
            messages.success(request, f'Deleted {count} movie reviews successfully!')

        else:
            messages.success(request, 'Invalid action.')

        return redirect('manipulate_movie_data')
    else:
        return render(request, 'manipulate_movie_data.html')
    






