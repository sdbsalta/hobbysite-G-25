# merchstore/urls.py

from django.urls import path
from .views import ProductTypeListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductCartView, ProductTransactionListView

urlpatterns = [
    path('items/', ProductTypeListView.as_view(), name='list'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('item/<int:pk>/edit/', ProductUpdateView.as_view(), name="product-update"),
    path('item/add/', ProductCreateView.as_view(), name='product-add'), 
    path('cart/',ProductCartView.as_view(), name='cart'),
    path('transactions/',ProductTransactionListView.as_view(), name='transactions'),
]

app_name = 'merchstore'
