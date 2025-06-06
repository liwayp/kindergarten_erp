from django.urls import path
from .views import meal_list, add_meal, meal_delete, count_portion_view,portion_log_list, product_notification, edit_meal, weekly_menu




urlpatterns = [
    path('', meal_list, name='meal-list'),
    path('add/', add_meal, name='add-meal'),
    path('<int:pk>/delete/',meal_delete , name='delete-meal'),
    path('meal/<int:meal_id>/count/',count_portion_view, name='count-portion'),
    path('portion/list/',portion_log_list, name='portion-list'),
    path('notification/', product_notification, name='product-notification'),
    path('<int:pk>/edit/', edit_meal, name='edit-meal'),
    path('menu/',weekly_menu , name='weekly_menu'),
]