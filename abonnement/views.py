from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from panier.models import *
from .models import *

# Create your views here.

class ListAbonnement(ListView):
    model = Pack
    context_object_name = 'packs'
    paginate_by = 20
    template_name = "abonnement.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      return context   
    
def detailAbonnement(request, pack_id):
   pack = get_object_or_404(Pack, id=pack_id)
   packs = Pack.objects.order_by('-created_at')[:4]
   context ={
        'pack': pack,
        'packs':packs,
    }
   return render(request, 'detail-abonnement.html',context)

@login_required
def get_abonnement_user(request):
   current_url = request.get_full_path()
   orders=Order.objects.filter(user=request.user)
   context ={
        'current_url': current_url,
        'orders':orders,
    }
   return render(request,'mes-abonnement.html', context)