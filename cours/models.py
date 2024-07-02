from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Cours(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True )
    name=models.CharField(max_length=200)
    description =models.TextField(null=True, blank=True)
    file=file=models.FileField()
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
       ordering = ['name']
