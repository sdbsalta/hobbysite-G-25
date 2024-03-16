# merchstore/admin.py

from django.contrib import admin
from .models import ProductType, Product


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'description', 'price')
    search_fields = ('name',)
    list_filter = ('product_type',)
    list_editable = ('price',)

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
