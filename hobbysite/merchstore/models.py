# merchstore/models.py

from django.db import models
from django.shortcuts import render
from django.urls import reverse

from user_management.models import Profile
from django.contrib.auth.models import User

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('On Sale', 'On Sale'),
        ('Out of Stock', 'Out of Stock'),
    ]

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType, 
        on_delete=models.SET_NULL, 
        null=True, 
        )
    owner = models.ForeignKey(
        Profile, 
        null=True,
        on_delete=models.CASCADE,
        blank=True,
        )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        
    def get_absolute_url(self):
        return reverse('merchstore:product-detail', args=[self.pk])
    
    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.status = 'Out of Stock'
        super(Product, self).save(*args, **kwargs)

class Transaction(models.Model):
    STATUS_CHOICES = (
        ('On cart', 'On cart'),
        ('To Pay', 'To Pay'),
        ('To ship', 'To Ship'),
        ('To receive', 'To Receive'),
        ('Delivered', 'Delivered'),
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
    
    def __str__(self):
        return str(self.product)
    