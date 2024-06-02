from django.db import models
from django.contrib.auth.models import AbstractUser

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