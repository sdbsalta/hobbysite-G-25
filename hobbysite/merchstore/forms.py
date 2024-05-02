# merchstore/forms.py

from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']  
        widgets = {
            'product_type': forms.Select(),
            'status': forms.Select(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'owner' in self.fields:
            self.fields['owner'].disabled = True
