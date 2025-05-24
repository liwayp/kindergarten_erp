from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Users

class CustomUserAdmin(BaseUserAdmin):
    model = Users
    list_display = ('email', 'name', 'role', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'role', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Users, CustomUserAdmin)