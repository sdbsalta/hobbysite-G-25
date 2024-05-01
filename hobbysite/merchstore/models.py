# merchstore/models.py

from django.db import models
from django.urls import reverse

from hobbysite.user_manangement.models import Profile

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        
    def get_absolute_url(self):
        return reverse('merchstore:product-detail', args=[self.pk])

class Transaction(models.Model):
    STATUS_CHOICES = (
        ('On cart'),
        ('To Pay'),
        ('To Ship'),
        ('To Receive'),
        ('Delivered'),
    )
    
    buyer = models.ForeignKey(
        Profile, 
        on_delete=models.SET_NULL, 
        null=True
        )
    product = models.ForeignKey(
        Product, 
        on_delete=models.SET_NULL, 
        null=True
        )
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)