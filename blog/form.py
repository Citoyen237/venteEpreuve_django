from django import forms
from .models import Category, Article
from tinymce.widgets import TinyMCE

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fiels =['user','name']
        exclude=['created_at','created_at']
        labels = {
            'user':'Utilisateur',
            'name':'Nom',
        }
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-select'}),

        }
    # def __init__(self, *args, **kwargs):
    #     super(CategoryForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].required = True

class ArticleForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30, 'class':'form-control'}))
    class Meta:
        model=Article
        fiels=['titre','user','file','image','category']
        exclude=['created_at','created_at']
        labels = {
            'user':'Utilisateur',
            'category':'Categorie',
            'titre':'Titre',
            # 'description':'Description',
            'image':'Image',
            'file':'Televerser un fichier',
        }
        widgets ={
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-select'}),
            'category':forms.Select(attrs={'class':'form-select'}),
            # 'description':forms.Textarea(attrs={'class':'form-control','row':4}),
            # 'image':forms.TextInput(attrs={'class':'form-control'}),
            # 'file':forms.TextInput(attrs={'class':'form-control'}),
        }