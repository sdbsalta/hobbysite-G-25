# merchstore/forms.py

from django import forms

from .models import Product, Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner'] 
        widgets = {
            'product_type': forms.Select(),
            'status': forms.Select(),
        }

class TransactionForm(forms.modelForm):
    class Meta:
        model = Transaction
        exclude = ['created_on']
    