# merchstore/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ProductType, Product

class ProductTypeListView(ListView):
    model = ProductType
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
