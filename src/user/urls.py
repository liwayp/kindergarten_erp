from django.urls import path
from .views import  login_view, logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

