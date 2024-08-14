from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from panier.models import Order, OrderItem
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    current_url = request.get_full_path()
    schools = School.objects.prefetch_related(
        'cursus__niveauxcur__filierescu',
        'cursus__niveauxcur__epreuveslevel', 
        'schoolep',
        'niveaux__epreuveslevel',
        'niveaux__filierescu__epreuvesstream',
        'cursus__epreuvescur',
        # 'cursus__niveaux__epreuves',
        # 'cursus__epreuves',       
        # Adjusted to match model definitions
        # 'cursus__filieres__epreuveslevel',
        # 'niveaux__filierescu__epreuvesstream',
        # 'niveaux__epreuveslevel',
        # 'epreuves'
    ).all()
    return render(request, 'list.html',{'schools':schools,'current_url':current_url})
# filierescu::level
def schoolCursusLevelFiliere(request, level_id):
   
    tests = Test.objects.filter(stream=level_id)
    schools = School.objects.prefetch_related(
        'cursus__niveauxcur__filierescu',
        'cursus__niveauxcur__epreuveslevel', 
        'schoolep',
        'niveaux__epreuveslevel',
        'niveaux__filierescu__epreuvesstream',
        'cursus__epreuvescur',
    ).all()
    return render(request, 'list_epreuve.html',{'schools':schools,'tests':tests})

def schoolCirrulumTest(request, cursus_id):
    tests = Test.objects.filter(curriculum_id=cursus_id)
    schools = School.objects.prefetch_related(
        'cursus__niveauxcur__filierescu',
        'cursus__niveauxcur__epreuveslevel', 
        'schoolep',
        'niveaux__epreuveslevel',
        'niveaux__filierescu__epreuvesstream',
        'cursus__epreuvescur',
    ).all()
    return render(request, 'list_epreuve.html',{'schools':schools,'tests':tests})

def schoolLevelFiliere(request, filiere_id):
    tests = Test.objects.filter(stream=filiere_id)
    schools = School.objects.prefetch_related(
        'cursus__niveauxcur__filierescu',
        'cursus__niveauxcur__epreuveslevel', 
        'schoolep',
        'niveaux__epreuveslevel',
        'niveaux__filierescu__epreuvesstream',
        'cursus__epreuvescur',
    ).all()
    return render(request, 'list_epreuve.html',{'schools':schools,'tests':tests})

def schoolLevelTest(request, niveau_id):
    tests = Test.objects.filter(level=niveau_id)
    schools = School.objects.prefetch_related(
        'cursus__niveauxcur__filierescu',
        'cursus__niveauxcur__epreuveslevel', 
        'schoolep',
        'niveaux__epreuveslevel',
        'niveaux__filierescu__epreuvesstream',
        'cursus__epreuvescur',
    ).all()
    return render(request, 'list_epreuve.html',{'schools':schools,'tests':tests})

def schoolTest(request, school_id):
    tests = Test.objects.filter(school_id=school_id)
    schools = School.objects.prefetch_related(
        'cursus__niveauxcur__filierescu',
        'cursus__niveauxcur__epreuveslevel', 
        'schoolep',
        'niveaux__epreuveslevel',
        'niveaux__filierescu__epreuvesstream',
        'cursus__epreuvescur',
    ).all()
    return render(request, 'list_epreuve.html',{'schools':schools,'tests':tests})

def schoolCursusLevelTest(request, level_id):
    tests = Test.objects.filter(level=level_id)
    schools = School.objects.prefetch_related(
        'cursus__niveauxcur__filierescu',
        'cursus__niveauxcur__epreuveslevel', 
        'schoolep',
        'niveaux__epreuveslevel',
        'niveaux__filierescu__epreuvesstream',
        'cursus__epreuvescur',
    ).all()
    return render(request, 'list_epreuve.html',{'schools':schools,'tests':tests})


def get_download_test(request, test_id):
  test = get_object_or_404(Test, id=test_id)
  school_id = test.school.id

  # Vérifier si l'école est présente dans les commandes de l'utilisateur
  user_orders = OrderItem.objects.filter(order__user=request.user, product__school=school_id)
  is_school_in_orders = user_orders.exists()

  if is_school_in_orders:
    # Vérifier si la date d'expiration a été atteinte pour les produits liés à cette école
    # vérifie si au moins un des produits commandés par l'utilisateur connecté et liés à l'école spécifiée a expiré.
    has_expired_items = any(item.is_expired for item in user_orders)
    if has_expired_items :
      messages.success(request,'Votre abonnement a cette ecole est expire')
      return redirect('index.ecole')
    else:
     document = get_object_or_404(Test, id=test_id)
     response = HttpResponse(document.file, content_type='application/octet-stream')
     response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
     return response
  else:
    #  abonnement ne correspond pas
    messages.success(request,'Vous n\'est pas abonner a cette ecole')
    return redirect('index.ecole')
 
   
  