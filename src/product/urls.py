from django.urls import path 
from .views import adding_pr, product_list_view, product_edit, product_delete


urlpatterns = [
    path('add/', adding_pr, name='add-pr'),
    path('list/', product_list_view, name='product_list'),
    path('products/<int:pk>/edit/', product_edit, name='product-edit'),
    path('products/<int:pk>/delete/', product_delete, name='product-delete'),
]

