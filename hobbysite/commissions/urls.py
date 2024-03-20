from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('list/', CommissionListView.as_view(), name='list'),
    path('detail/<int:pk>/', CommissionDetailView.as_view(), name='comment-detail'),
]

# This might be needed, depending on your Django version
app_name = "commissions"