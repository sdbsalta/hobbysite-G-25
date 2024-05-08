# merchstore/views.py

from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from user_management.models import Profile

from .models import Product, ProductType, Transaction
from .forms import ProductForm, TransactionForm

class ProductTypeListView(ListView):
    model = Product
    template_name = 'merchstore/product_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_type'] = ProductType.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'merchstore/product_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = TransactionForm()
        return ctx
    
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        product = self.get_object()
        
        if form.is_valid():
            if request.user.is_authenticated:
                transaction = form.save(commit=False)
                transaction.product = product
                transaction.buyer = request.user.profile
                transaction.status = "On Cart"
                transaction.save()
                
                product.stock -= transaction.amount
                product.save()
                return redirect('merchstore:cart')
            else:
                return redirect(reverse('login') + '?next=' + request.path)
        return self.render_to_response(self.get_context_data(form=form))

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'merchstore/product_create.html'
    
    def get_success_url(self):
        return reverse_lazy("merchstore:list")

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        form.fields['owner'].initial = Profile.objects.get(user=self.request.user)
        form.fields['owner'].disabled = True
        
        context['form'] = form
        return context

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'merchstore/product_update.html'
    
    def form_valid(self, form):
        product = self.get_object()
        if form.is_valid():
            if product.stock == 0:
                form.cleaned_data['status'] = 'Out of Stock'
            form.instance.owner = Profile.objects.get(user=self.request.user)
        product.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        form.fields['owner'].initial = Profile.objects.get(user=self.request.user)
        form.fields['owner'].disabled = True
        
        context['form'] = form
        return context

class ProductCartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'merchstore/cart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.all()
        context['product'] = Product.objects.all()
        return context

class ProductTransactionListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'merchstore/transaction_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.all()
        context['profile'] = Profile.objects.all()
        return context
        