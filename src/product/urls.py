from django.urls import path 
from .views import adding_pr, product_list_view


urlpatterns = [
    path('add/', adding_pr, name='add-pr'),
    path('list/', product_list_view, name='product_list'),
]

