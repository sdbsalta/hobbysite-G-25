# merchstore/forms.py

from django import forms
from django.contrib import admin

from user_management.models import Profile

from .models import Product, Transaction

class ProductForm(forms.ModelForm):
    
    owner = forms.ModelChoiceField(required=False, queryset=Profile.objects)
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_type': forms.Select(),
            'status': forms.Select(),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['product', 'buyer', 'status', 'created_on']
        
    