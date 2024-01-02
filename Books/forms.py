from django import forms
from Books.models import CommentModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name','body']
