from django.urls import path
from .views import main_page, dashboard, logout_view


urlpatterns = [
    path('', main_page, name='main'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),

]


