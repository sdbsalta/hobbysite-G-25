from django.contrib import admin

from .models import ThreadCategory, Thread, Comment

class ThreadAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'entry', 'image')

    def get_fields(self, request, obj=None):
        if obj:
            return ('title', 'category', 'entry', 'image')
        return self.fields

admin.site.register(ThreadCategory)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment)