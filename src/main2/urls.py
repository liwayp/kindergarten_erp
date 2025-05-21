from django.urls import path
from .views import main_page, login_page

urlpatterns = [
    path('', main_page, name='main'),
    path('login/', login_page, name='main2'),
]
