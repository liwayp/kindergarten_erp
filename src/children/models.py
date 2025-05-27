from django.db import models
from user.models import Users
from django.utils import timezone


class ChildGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Children(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField( default=timezone.now)
    raw_password = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey(
    Users,
    on_delete=models.CASCADE,  
    related_name='children',
    limit_choices_to={'role': 'parents'}
)
    group = models.ForeignKey(ChildGroup, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    

