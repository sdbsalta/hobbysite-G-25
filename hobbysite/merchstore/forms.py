# merchstore/forms.py

from django import forms

from .models import Product

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'