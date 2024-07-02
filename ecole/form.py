from django.db import models
from django import forms
from .models import *
from django.contrib.auth.models import AbstractUser


class SchoolForm(forms.ModelForm):
     class Meta:
        model=School
        fiels =['user','name','city','slug']
        exclude=['created_at','created_at']
        labels = {
            'user':'Utilisateur',
            'name':"Nom de l'ecole",
            'ville':'Ville',
            'slug':'Abreviation'
        }
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-select'}),
        }

class CurcusForm(forms.ModelForm):
    class Meta:
        model= Curriculum
        fiels =['user','name','school']
        exclude=['created_at','created_at']
        labels = {
            'user':'Utilisateur',
            'name':"Libelle",
            'school':'Ecole',
        }
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-select'}),
            'school':forms.Select(attrs={'class':'form-select'}),
        }
     
class LevelForm(forms.ModelForm):
    class Meta:
        model=Level
        fiels=['user','name','school','curriculum']
        exclude=['created_at','created_at']
        labels = {
            'user':'Utilisateur',
            'name':"Libelle",
            'curriculum':'Cursus',
            'school':'Ecole'
        }
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'curriculum':forms.Select(attrs={'class':'form-select'}),
            'school':forms.Select(attrs={'class':'form-select'}),
            'user':forms.Select(attrs={'class':'form-select'}),
        }

class StreamForm(forms.ModelForm):
    class Meta:
        model=Stream
        fiels=['user','name','curriculum','level']
        exclude=['created_at','created_at']
        labels = {
            'user':'Utilisateur',
            'name':"Libelle",
            'curriculum':'Cursus',
            'level':'Niveau'
        }
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'curriculum':forms.Select(attrs={'class':'form-select'}),
            'level':forms.Select(attrs={'class':'form-select'}),
            'user':forms.Select(attrs={'class':'form-select'}),
        }

class TestForm(forms.ModelForm):
    class Meta:
        model=Test
        fiels=['user','annee','name','stream','file','curriculum','level']
        exclude=['created_at','created_at']
        labels = {
            'user':'Utilisateur',
            'name':"Libelle",
            'stream':"Filiere",
            'file':"Epreuve",
            'Anne':"Annee",
            'curriculum':'Cursus',
            'level':'Niveau'
        }
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'curriculum':forms.Select(attrs={'class':'form-select'}),
            'level':forms.Select(attrs={'class':'form-select'}),
            'annee':forms.TextInput(attrs={'class':'form-control'}),
            'stream':forms.Select(attrs={'class':'form-select'}),
            'user':forms.Select(attrs={'class':'form-select'}),
        }


# class CustomUser(AbstractUser):
#     school = models.ForeignKey('School', on_delete=models.CASCADE)
#     subscription_status = models.BooleanField(default=False)

'''liste les epreuve en fonction de leur hearchie'''
# from django.shortcuts import render
# from .models import School

# def display_hierarchy(request):
#     schools = School.objects.all()
#     context = {'schools': schools}
#     return render(request, 'your_template.html', context)

# {% for school in schools %}
#     <h1>{{ school.name }}</h1>
#     {% for curriculum in school.curriculum_set.all %}
#         <h2>{{ curriculum.name }}</h2>
#         {% for level in curriculum.level_set.all %}
#             <h3>{{ level.name }}</h3>
#             {% for field in level.field_set.all %}
#                 <h4>{{ field.name }}</h4>
#                 {% for test in field.test_set.all %}
#                     <p>{{ test.name }}</p>
#                 {% endfor %}
#             {% endfor %}
#         {% endfor %}
#     {% endfor %}
# {% endfor %}

'''school hierachie 2'''

# from django.shortcuts import render
# from .models import School, Curriculum, Level, Stream, Test

# def school_hierarchy(request, school_id):
#     school = School.objects.get(id=school_id)
#     curriculums = Curriculum.objects.filter(school=school)
#     hierarchy = {
#         "school": school.name,
#         "curriculums": []
#     }
#     for curriculum in curriculums:
#         curriculum_dict = {
#             "curriculum": curriculum.name,
#             "levels": []
#         }
#         levels = Level.objects.filter(curriculum=curriculum)
#         for level in levels:
#             level_dict = {
#                 "level": level.name,
#                 "streams": []
#             }
#             streams = Stream.objects.filter(level=level)
#             for stream in streams:
#                 stream_dict = {
#                     "stream": stream.name,
#                     "tests": []
#                 }
#                 tests = Test.objects.filter(stream=stream)
#                 for test in tests:
#                     stream_dict["tests"].append(test.name)
#                 level_dict["streams"].append(stream_dict)
#             curriculum_dict["levels"].append(level_dict)
#         hierarchy["curriculums"].append(curriculum_dict)
#     return render(request, 'school_hierarchy.html', {'hierarchy': hierarchy})

# <h1>{{ hierarchy.school }}</h1>
# {% for curriculum in hierarchy.curriculums %}
#     <h2>{{ curriculum.curriculum }}</h2>
#     {% for level in curriculum.levels %}
#         <h3>{{ level.level }}</h3>
#         {% for stream in level.streams %}
#             <h4>{{ stream.stream }}</h4>
#             {% for test in stream.tests %}
#                 <p>{{ test }}</p>
#             {% endfor %}
#         {% endfor %}
#     {% endfor %}
# {% endfor %}