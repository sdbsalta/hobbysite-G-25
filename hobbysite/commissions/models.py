from django.db import models
from django.shortcuts import render
from django.urls import reverse

from user_management.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return self.title

class Job(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='job')
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    STATUS_CHOICES = [('Open', 'Open'), ('Full', 'Full'),]
    status = models.CharField(choices=STATUS_CHOICES, default='Open')
    
    class Meta:
        ordering = [
            'status',
            '-manpower_required',
            'role'
            ]
        
    #def __str__(self):
    #    return self.title

    def get_absolute_url(self):
        return reverse('commissions:job-detail', args=[self.pk])
    
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_application')
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', '-applied_on']

    def __str__(self):
        return str(self.job) # check    