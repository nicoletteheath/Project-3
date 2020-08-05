from django import forms
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image']
        widgets = {
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form',
                    'class': 'inputbox',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form',
                    'class': 'inputbox'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form',
                    'class': 'inputbox',
                    'placeholder': 'Enter Comments Here'
                }
            )
        }