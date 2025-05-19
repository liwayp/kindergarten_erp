from django.db import models
from product.models import Products
from user.models import Users

class Meals(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)

class PortionEstimates(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    possible_portions = models.IntegerField()
    calculated_at = models.DateTimeField(auto_now_add=True)


