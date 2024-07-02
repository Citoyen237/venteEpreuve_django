from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from tinymce.models import HTMLField
# Create your models here.

'''model category'''
class Category(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True )
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

'''model article'''
class Article(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    titre=models.CharField(max_length=200)
    description=HTMLField()
    file=models.FileField(null=True, blank=True) 
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

# bank:Rend ce champ facultatif dans les formulaires Django.
# null:Rend ce champ facultatif dans les formulaires Django.
# librairie pillow:pour la manipulation d'image.



