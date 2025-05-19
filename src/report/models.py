from django.db import models

class MonthlyReports(models.Model):
    month_year = models.CharField(max_length=7, null=True, blank=True)
    total_served = models.IntegerField(null=True, blank=True)
    total_possible = models.IntegerField(null=True, blank=True)
    difference_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 