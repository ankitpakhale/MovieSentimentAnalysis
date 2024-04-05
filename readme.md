# Movie Sentiment Analysis

## About
Movie Sentiment Analysis is a Django web application that allows users to submit movie reviews and performs sentiment analysis on them. The application also provides features to manipulate movie data, such as adding or deleting reviews.

## Technologies Used
- Python: Programming language used for backend development.
- Django: Web framework used for building the application.
- NLTK: Natural Language Toolkit library used for text preprocessing and sentiment analysis.
- Joblib: Library used for model persistence.
- Other Dependencies: See requirements.txt for a list of all dependencies.

## Project Setup
To set up the project, follow these steps:

### Prerequisites
- Python 3.8.10
- Django

### Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory.

### Setup
1. Clone the project repository:
    ```bash
    git clone https://github.com/ankitpakhale/MovieSentimentAnalysis.git
    ```

2. Navigate to the project directory:
    ```bash
    cd MovieSentimentAnalysis
    ```

3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
    ```bash
    venv\Scripts\activate
    ```
    - On Linux:
    ```bash
    source venv/bin/activate
    ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup (Optional)
By default, the project uses SQLite as the database backend. You can modify the `DATABASES` setting in `settings.py` to use a different database like PostgreSQL or MySQL.

### Running the Application
1. Apply migrations:
    ```bash
    python manage.py migrate
    ```
2. Start the development server:
    ```bash
    python manage.py runserver
    ```
3. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage
- Submit Movie Review: Visit the homepage to submit a movie review. All fields are optional.
- Manipulate Movie Data: Use the provided form to add or delete movie reviews. You can choose the action and specify the number of reviews to manipulate.


