from django.db import models

class Permissions(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class Roles(models.Model):
    role_sistem = (
        ('manager', 'manager'),
        ('cooker', 'cooker')
        )
    name = models.CharField(max_length=20,choices=role_sistem)
    description = models.TextField(null=True, blank=True)


class RolePermissions(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permissions, on_delete=models.CASCADE)


class Users(models.Model):
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    password_hash = models.CharField(max_length=255)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
