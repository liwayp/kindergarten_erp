from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    minimum_threshold = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

