from django.urls import path
from .views import  login_view, add_employee, employee_list, edit_employee, delete_employee
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view,  name='login'),
    path('add/', add_employee, name='add_employee'),
    path('employee-list/', employee_list, name='employee-list'),
    path('employee/<int:pk>/edit/', edit_employee, name='edit_employee'),
    path('employee/<int:pk>/delete/', delete_employee, name='delete_employee'),
    # path('logout/', logout_view, name='logout'),
]

