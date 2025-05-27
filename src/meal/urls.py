from django.urls import path
from .views import meal_list, add_meal




urlpatterns = [
    path('//', meal_list, name='meal-list'),
    path('/add/', add_meal, name='add-meal'),
    # path('/<int:pk>/edit/', edit_meal, name='edit-meal'),

]