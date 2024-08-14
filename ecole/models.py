from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
'''ecole'''
class School(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    '''meta donnee'''
    class Meta:
       ordering = ['name']

'''curcus'''
class Curriculum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='cursus')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
       ordering = ['name']

'''niveau'''
class Level(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True )
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, null=True, blank=True, related_name='niveauxcur')
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True,related_name='niveaux')
    name = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
       ordering = ['name']

'''filiere'''
class Stream(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, null=True, blank=True,related_name='filieres')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True,related_name='filierescu')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
       ordering = ['name']

'''epreuve'''
class Test(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=200)
    annee=models.CharField(max_length=200)
    file=models.FileField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True,related_name='schoolep')
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True,related_name='epreuvesstream')
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, null=True, blank=True,related_name='epreuvescur')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=True,related_name='epreuveslevel')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
       ordering = ['name']
