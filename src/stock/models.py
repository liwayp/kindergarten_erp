from django.db import models
from product.models import Products

class Stock(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

