from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

from .models import Profile


class ProfileView(DetailView):
    model = Profile
    template_name = ""