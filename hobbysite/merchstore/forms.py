# merchstore/forms.py

from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'product_type', 'status', 'stock', 'price']
        widgets = {
            'product_type': forms.Select(),
            'status': forms.Select(),
        }