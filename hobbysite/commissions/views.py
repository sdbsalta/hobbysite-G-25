from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from user_management.models import Profile

from .models import Commission, Job, JobApplication
# import from forms if needed later
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Commission, Job, JobApplication

class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'
    ordering = ['-created_on']

class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commissions_detail.html'

class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commissions_form.html'
    fields = [
        'title',
        'description',
        'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    template_name = 'commissions_form.html'
    fields = ['title', 'description', 'status']

    def form_valid(self, form):
        form.instance.updated_on = timezone.now()
        return super().form_valid(form)
