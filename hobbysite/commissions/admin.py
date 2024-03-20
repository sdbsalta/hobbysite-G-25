from django.contrib import admin
from .models import Commission, Comment

# Register your models here.

class CommissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'people_required', 'created_on', 'updated_on')
    list_filter = ('created_on',)
    search_fields = ('title',)
    ordering = ('created_on',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commission', 'created_on', 'updated_on')
    list_filter = ('created_on',)
    search_fields = ('entry', 'commission__title')
    ordering = ('-created_on',)

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)