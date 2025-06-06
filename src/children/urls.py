from django.urls import path
from .views import child_registration, registration_history, edit_child, child_delete, group_list, add_group, group_detail, edit_group, delete_group


urlpatterns = [
    path('register/', child_registration, name='children_rg'),
    path('list/', registration_history , name='children_list'),
    path('edit/<int:pk>/', edit_child, name='edit_child'),
    path('delete/<int:pk>/', child_delete, name='delete_child'),
    path('groups/', group_list, name='group_list'),
    path('group/add/', add_group, name='add_group'),
    path('groups/<int:group_id>/', group_detail, name='group_detail'),
    path('groups/<int:pk>/edit/', edit_group, name='edit_group'),
    path('groups/<int:pk>/delete/', delete_group, name='delete_group'),
]
