from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView
from ecole.models import *
from django.views.generic.edit import UpdateView, DeleteView, CreateView

# from django.contrib.auth.decorators import login_required

# Create your views here.

'''index'''
'''verfication si l'utilisateur est connecter'''
# @login_required

'''verifier si l'utilisateur connecter est superadmin'''
# @user_passes_test(lambda u: u.is_superuser, login_url='/login/')
def index(request):
   if not request.user.is_authenticated:
      return render(request,'partial/404.html')
   
   return render(request, 'app.html')

'''manipulation des ecoles'''
class ListSchool(ListView):
    model = School
    context_object_name = 'schools'
    paginate_by = 10
    template_name = "school/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      return context