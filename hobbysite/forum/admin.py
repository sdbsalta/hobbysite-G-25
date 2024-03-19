from django.contrib import admin

from .models import PostCategory, Post


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on')
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)