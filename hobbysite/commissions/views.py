from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from user_management.models import Profile

from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobForm, JobApplicationForm

class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions/commissions_list.html'
    ordering = ['-created_on']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_commissions'] = Commission.objects.filter(author=self.request.user).order_by('-created_on')
            context['user_applications'] = JobApplication.objects.filter(applicant=self.request.user.profile).order_by('-applied_on')
        return context

class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = 'commissions/commissions_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
<<<<<<< HEAD
        context['jobs'] = Job.objects.filter(commission=self.object)
=======
        jobs = Job.objects.filter(commission=self.object)

        for job in jobs:
            job.is_full = job.job_application_set.filter(status='Accepted').count() >= job.manpower_required

        context['jobs'] = jobs
        context['total_manpower_required'] = sum(job.manpower_required for job in jobs)
        context['total_open_manpower'] = sum(job.manpower_required - job.job_application_set.filter(status='Accepted').count() for job in jobs)
>>>>>>> commissions_poch
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        job_id = request.POST.get('job_id')
        job = get_object_or_404(Job, id=job_id)
        JobApplication.objects.create(job=job, applicant=request.user.profile)
        return redirect('commissions:commission_detail', pk=self.object.pk)

class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commissions/commissions_form.html'
    fields = [
        'title',
        'description',
<<<<<<< HEAD
        'status'
        ]
    login_url = '/login/'
=======
        'status',
        'created_on',
        'updated_on'
        ]
    login_url = 'login'
>>>>>>> commissions_poch

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        form.fields['author'].initial = Profile.objects.get(user=self.request.user)
        form.fields['author'].disabled = True
        form.fields['created_on'].disabled = True
        form.fields['updated_on'].disabled = True

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    template_name = 'commissions/commissions_form.html'
<<<<<<< HEAD
    fields = ['title', 'description', 'status']
    login_url = '/login/'
=======
    fields = [
        'title',
        'description',
        'status',
        'created_on',
        'updated_on'
        ]
    login_url = 'login'
>>>>>>> commissions_poch

    def form_valid(self, form):
        commission = form.save(commit=False)
        if all(job.status == 'Full' for job in commission.job.all()):
            commission.status = 'Full'
        commission.updated_on = timezone.now()
        commission.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        form.fields['author'].initial = Profile.objects.get(user=self.request.user)
        form.fields['author'].disabled = True
        form.fields['created_on'].disabled = True