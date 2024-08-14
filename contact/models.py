from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    email=models.EmailField()
    Message=models.TextField()
    response=models.TextField(blank=True, null=True)
    is_read=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    @classmethod
    def unread_count(cls):
        return cls.objects.filter(is_read=False).count()
    
    def __str__(self):
        return self.email
