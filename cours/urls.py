from django.urls import path
from .views import *

urlpatterns = [
    path('',cours, name='cours'),
    path('apprentissage/',apprentissage, name='apprentissage'),
    path('download/<int:file_id>/', download_file, name='download_file'),
]
