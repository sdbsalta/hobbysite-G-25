# hobbysite/blog/admin.py

from django.contrib import admin
from .models import ArticleCategory, Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'entry', 'header_image')

    def get_fields(self, request, obj=None):
        if obj:
            return ('title', 'category', 'entry', 'header_image')
        return self.fields

admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
