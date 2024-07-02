from django.urls import path
from .views import *

urlpatterns = [
    path('' ,getcontact, name='front.contact'),
]
