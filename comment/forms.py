from .models import Comment
from django import forms



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('rating', 'author', 'email', 'text',)
        labels = {
        	'author': ('Your Name'),
        	'text': ('Tell us about your experience...')
        }
        widgets = {'rating':forms.HiddenInput()}