from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    email=models.EmailField()
    Message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email
