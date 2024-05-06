from django import forms

from .models import Thread, Comment


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'category', 'entry', 'image')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields.pop('author')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('entry',)