from django import forms
from .models import Pack


class PackForm(forms.ModelForm):
    class Meta:
        model =Pack
        fiels = ['title','school','prix','oldPrix','duree','image','decription','user']
        exclude = ['created_at','updated_at']
        labels= {'title':'Titre',
                 'school':'Ecole',
                 'duree':'Duree',
                 'prix':'Prix',
                 'description':'Description',
                 'image':'Image',
                 'user':'Utilisateur',
                 'oldPrix':'Ancien prix',
                }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'school':forms.Select(attrs={'class':'form-select'}),
            'duree':forms.TextInput(attrs={'class':'form-control'}),
            'prix':forms.NumberInput(attrs={'class':'form-control'}),
            'aldPrix':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','row':3}),
            'user':forms.Select(attrs={'class':'form-select'}),
        }