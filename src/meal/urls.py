from django.urls import path
from .views import meal_list, add_meal

urlpatterns = [
    path('meal/', meal_list, name='meal-list'),
    path('meal/add/', add_meal, name='add-meal'),
]