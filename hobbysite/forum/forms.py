from django import forms

from .models import Thread, Comment
from user_management.models import Profile


class ThreadForm(forms.ModelForm):
    
    author = forms.ModelChoiceField(required=False, queryset=Profile.objects)

    class Meta:
        model = Thread
        fields='__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('entry',)
