# merchstore/views.py

from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, ProductType, Transaction
from .forms import ProductForm, TransactionForm

class ProductTypeListView(ListView):
    model = Product
    template_name = 'product_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_type'] = ProductType.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    
    def form_valid(self, form):
        form.instance.buyer = self.request.user.profile
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            product = self.get_object()
            product.stock -= form.cleaned_data['quantity']
            product.save()
            return redirect('product_detail', pk=product.pk) 
        return self.render_to_response(self.get_context_data(form=form))


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    
    def get_success_url(self):
        return reverse_lazy("merchstore:list")

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_detail.html'

class ProductCartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'cart.html'
    
class TransactionView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction.html'

class ProductTransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction_list.html'
    

    

        