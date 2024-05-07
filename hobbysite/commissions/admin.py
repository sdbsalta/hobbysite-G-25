from django.contrib import admin
from .models import Commission, Job, JobApplication

# Register your models here.

class CommissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_on', 'updated_on']
    search_fields = ('title',)
    ordering = ('created_on',)

class JobAdmin(admin.ModelAdmin):
    list_display = ['commission', 'role', 'manpower_required', 'status']
    ordering = ('status', '-manpower_required', 'role')

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['job', 'applicant', 'status', 'applied_on']
    ordering = ('status', '-applied_on')    

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)