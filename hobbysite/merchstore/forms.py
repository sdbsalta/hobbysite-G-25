# merchstore/forms.py

from django import forms

from .models import Product, Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'owner', 'product_type', 'description','price','stock', 'status']
        widgets = {
            'product_type': forms.Select(),
            'status': forms.Select(),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['created_on']
        
    