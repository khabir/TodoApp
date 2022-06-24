import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    deadline = models.DateTimeField(null=True)