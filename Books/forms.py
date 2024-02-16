from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({
            'class': 'bg-gray-100 rounded-lg border border-gray-300 py-2 px-4 w-full',
            'placeholder': 'Write your comment here...',
             'rows': 7, 
             'cols': 60, 
        })

    class Meta:
        model = CommentModel
        fields = ['body']
