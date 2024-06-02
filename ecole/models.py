from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''ecole'''
class School(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    '''meta donnee'''
    class Meta:
       ordering = ['name']

'''curcus'''
class Curriculum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ['name']

'''niveau'''
class Level(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ['name']
'''filiere'''
class Stream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ['name']

'''epreuve'''
class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200)
    annee=models.CharField(max_length=200)
    file=models.FileField()
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ['name']
