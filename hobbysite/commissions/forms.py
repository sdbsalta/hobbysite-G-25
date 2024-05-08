from django import forms
from django.contrib import admin

from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = [
            'title',
            'description',
            'status',
            'created_on',
            'updated_on',
            'author'
            ] 
        widgets = {
            'status': forms.Select(choices=Commission.STATUS_CHOICES),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']
        widgets = {
            'status': forms.Select(choices=Job.STATUS_CHOICES),
        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []