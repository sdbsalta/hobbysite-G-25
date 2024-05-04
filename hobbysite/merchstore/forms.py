# merchstore/forms.py

from django import forms

from .models import Product
from user_management.models import Profile

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner'] 
        widgets = {
            'product_type': forms.Select(),
            'status': forms.Select(),
        }
    
    