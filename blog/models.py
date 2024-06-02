from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''model category'''
class Category(models.Model):
    libelle=models.CharField(max_length=200)
    def __str__(self):
        return self.libelle

'''model article'''
class Article(models.Model):
    user:models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titre=models.CharField(max_length=200)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# bank:Rend ce champ facultatif dans les formulaires Django.
# null:Rend ce champ facultatif dans les formulaires Django.
# librairie pillow:pour la manipulation d'image.



