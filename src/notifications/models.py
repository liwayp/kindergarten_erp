from django.db import models
from user.models import Users

class Notifications(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

