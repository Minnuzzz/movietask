from django import forms
from .models import movie, Review

from django import forms
from .models import movie,Review

class movieform(forms.ModelForm):
    class Meta:
        model = movie
        fields = ['name', 'desc', 'img', 'date', 'actors', 'youtube_link','category']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']