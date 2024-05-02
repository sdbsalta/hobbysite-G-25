from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profile_detail.html"