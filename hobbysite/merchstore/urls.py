# merchstore/urls.py

from django.urls import path
from .views import ProductTypeListView, ProductDetailView

app_name = 'merchstore'

urlpatterns = [
    path('items/', ProductTypeListView.as_view(), name='list'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

app_name = 'tasks'