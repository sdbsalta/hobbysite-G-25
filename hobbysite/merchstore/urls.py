# merchstore/urls.py

from django.urls import path
from .views import ProductTypeListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('items/', ProductTypeListView.as_view(), name='list'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('recipe/add/', ProductCreateView.as_view(), name='product-add'),
]

app_name = 'merchstore'
