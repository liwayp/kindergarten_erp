from django.urls import path
from .views import child_registration, registration_history


urlpatterns = [
    path('/register/', child_registration, name='children_rg'),
    path('/list/', registration_history , name='children_list')
]
