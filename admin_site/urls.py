from django.urls import path
from .views import *

urlpatterns = [
    path('', index ,name='dashboard.index'),
    path('ecole/',ListSchool.as_view(),name='ecole.list')
]
