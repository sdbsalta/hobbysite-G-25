# merchstore/admin.py

from django.contrib import admin
from .models import ProductType, Product, Transaction
    
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'owner', 'price', 'stock',)
    search_fields = ('name',)
    list_filter = ('product_type',)
    list_editable = ('price', 'stock',)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'product', 'amount', 'status', 'created_on']
    readonly_fields = ('buyer',)
    list_filter = ['status', 'created_on']
    search_fields = ['buyer__user__username', 'product__name']
    
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
