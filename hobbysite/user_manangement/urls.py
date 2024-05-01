#user_management/urls.py

from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
]

app_name = 'user_management'