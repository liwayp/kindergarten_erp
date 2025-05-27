from django.db import models
from product.models import Products
from user.models import Users

class Meal(models.Model):
    type_of_meal=[

        (1, "breakfast"),
        (2, "lunch"),
        (3, "snack")
    ]
    
    type=models.IntegerField(choices=type_of_meal)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Products, related_name='meals')

    def __str__(self):
        return self.name



class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.product.name



