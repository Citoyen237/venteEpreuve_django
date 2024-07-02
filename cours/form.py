from django import forms
from .models import Cours

class CoursForm(forms.ModelForm):
    class Meta:
        model=Cours
        fiels =['user','name','description','file','image']
        exclude=['created_at','created_at']
        labels = {
            'user':'Utilisateur',
            'name':'Nom',
            'description':'Description',
            'file':'fichier'
        }
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','row':4}),
            'user':forms.Select(attrs={'class':'form-select'}),

        }