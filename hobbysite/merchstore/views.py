# merchstore/views.py

from django.views.generic import ListView, DetailView

from .models import Product

class ProductTypeListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
