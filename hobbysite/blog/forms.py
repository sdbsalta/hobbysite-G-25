# hobbysite/blog/forms.py

from django import forms

from user_management.models import Profile
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    
    author = forms.ModelChoiceField(required=False, queryset=Profile.objects)
    class Meta:
        model = Article
        fields = ('title', 'category', 'entry', 'header_image')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('entry',)