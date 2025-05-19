from django.db import models
from product.models import Products
from user.models import Users

class Inventory(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
