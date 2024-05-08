from django.urls import path
from .views import CommissionListView, CommissionDetailView, CommissionCreateView, CommissionUpdateView

urlpatterns = [
    path('list/', CommissionListView.as_view(), name='list'),
    path('detail/<int:pk>/', CommissionDetailView.as_view(), name='commission_detail'),
    path('add/', CommissionCreateView.as_view(), name='commission_add'),
    path('<int.pk>/edit/', CommissionUpdateView.as_view(), name='commission_update'), 
]

# This might be needed, depending on your Django version
app_name = "commissions"