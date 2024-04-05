from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['movie_title', 'review_text']
        # All fields are non-required now
        widgets = {
            'movie_title': forms.TextInput(attrs={'placeholder': 'Enter movie title'}),
            'review_text': forms.Textarea(attrs={'placeholder': 'Enter your review'}),
        }

class ManipulateDataForm(forms.Form):
    manipulate_action = forms.ChoiceField(choices=[('add', 'Add Movie Reviews'), ('delete', 'Delete Added Movie Reviews')])
    manipulate_count = forms.IntegerField(min_value=1, initial=1)
