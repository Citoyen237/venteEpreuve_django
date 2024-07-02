from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    schools = School.objects.prefetch_related('cursus__niveaux__filieres__filierescu__epreuvesstream__epreuvescur__epreuveslevel').all()
    return render(request, 'list.html',{'schools':schools})
# filierescu::level