from django.db import models
from meal.models import Meal




# class WeeklyMealReport(models.Model):
#     start_date = models.DateField()  
#     end_date = models.DateField()    
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         unique_together = ('start_date', 'end_date')
#         ordering = ['-start_date']

#     def __str__(self):
#         return f"Неделя: {self.start_date} — {self.end_date}"




# class DailyMealRecord(models.Model):
#     report = models.ForeignKey(WeeklyMealReport, related_name='daily_meals')
#     date = models.DateField()
#     meal_type = models.CharField(
#         max_length=10,
#         choices=Meals.type_of_meal
#     )
#     meal = models.ForeignKey(Meals, null=False)
#     served_portions = models.IntegerField(null=True)
#     notes = models.TextField(null=True)
    
#     class Meta:
#         unique_together = ('report', 'date', 'meal_type')
#         ordering = ['date', 'meal_type']

#     def __str__(self):
#         return f"{self.get_meal_type_display()} - {self.date}"

