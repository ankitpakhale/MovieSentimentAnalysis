import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from .constants import MODEL_PATH, TFIDF_VECTORIZER_PATH

# Load the TF-IDF vectorizer using the path from constants
tfidf_vectorizer = joblib.load(TFIDF_VECTORIZER_PATH)


def load_sentiment_model(model_path):
    return joblib.load(model_path)

def preprocess_review(review_text):
    # Convert text to lowercase
    review_text = review_text.lower()
    
    # Remove special characters and punctuation
    review_text = re.sub(r'[^a-zA-Z\s]', '', review_text)
    
    # Tokenize the review text
    tokens = word_tokenize(review_text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join tokens back into a string
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text

def classify_sentiment(model, review_text):
    # Preprocess the review text
    preprocessed_text = preprocess_review(review_text)
    
    # Transform the preprocessed text using the loaded TF-IDF vectorizer
    preprocessed_text_vectorized = tfidf_vectorizer.transform([preprocessed_text])
    
    # Predict sentiment using the model
    sentiment = model.predict(preprocessed_text_vectorized)[0]
    
    return sentiment
