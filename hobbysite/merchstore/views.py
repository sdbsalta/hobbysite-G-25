# merchstore/views.py

from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product

class ProductTypeListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        all_products = Product.objects.exclude(user=self.request.user)
        user_products = Product.objects.filter(user=self.request.user)

        context['create_product_url'] = reverse_lazy('create_product')
        context['all_products'] = all_products
        context['user_products'] = user_products
        
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
