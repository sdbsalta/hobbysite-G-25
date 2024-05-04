# merchstore/forms.py

from django import forms
from django.contrib import admin

from .models import Product, Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner',]
        widgets = {
            'product_type': forms.Select(),
            'status': forms.Select(),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['product', 'buyer', 'status', 'created_on']
        
    