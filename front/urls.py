from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="front.index"),
    path('page-not-found/',pagenotfound,name='no_access')
]
