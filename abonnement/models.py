from django.db import models
from ecole.models import School
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Pack(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True )
    title = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    oldPrix=models.IntegerField()
    prix = models.IntegerField()
    duree = models.IntegerField()
    image=models.ImageField()
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
       ordering = ['title']