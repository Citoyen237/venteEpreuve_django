from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView
from ecole.models import *
from ecole.form import *
from abonnement.models import Pack
from abonnement.form import PackForm
from cours.models import Cours
from cours.form import CoursForm
from blog.models import Category, Article
from blog.form import CategoryForm, ArticleForm
from django.urls import reverse_lazy
from django.contrib import messages
from contact.models import Message
from auth_app.models import CustomUser as User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from panier.models import *
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from ecole.utils import get_expired_products
from .form import ReponseForm
from django.core.mail import send_mail


# from django.contrib.auth.decorators import login_required
def no_access(request):
    return render(request, 'partial/404.html')

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('no_access')
# Create your views here.

'''index'''
# Vérifier si l'utilisateur est un super administrateur
def superuser_required(user):
    return user.is_superuser
'''verfication si l'utilisateur est connecter'''
# @login_required

'''verifier si l'utilisateur connecter est superadmin'''
# @user_passes_test(lambda u: u.is_superuser, login_url='/login/')
@login_required
@user_passes_test(superuser_required, login_url='/login/')
def indexAdmin(request):
   '''verifier si l'utilisateur est superadmin'''
   if not request.user.is_authenticated:
      return render(request,'partial/404.html')
   
   '''recuperer l'url'''
   # expired_products = get_expired_products()
   orders=Order.objects.all()
   current_url = request.get_full_path()
   context = {
        'current_url': current_url,
        'orders':orders,
      #   'expired_products':expired_products
    }
   return render(request, 'indexAdmin.html',context)
# class DashboardList(ListView, LoginRequiredMixin, SuperuserRequiredMixin):
#    model=User
#    context_object_name = 'users'
#    paginate_by = 10
#    template_name = "indexAdmin.html"

#    def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context['current_url'] = self.request.path
#       return context   

'''manipulation des ecoles'''
class ListSchool(ListView,LoginRequiredMixin, SuperuserRequiredMixin):
    model = School
    context_object_name = 'schools'
    paginate_by = 10
    template_name = "school/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urlsA']=['']
      context['urls']=['/dashboard/curcus/', '/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
class CreateSchool(CreateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = School
   form_class=SchoolForm
   template_name="school/create-school.html"
   success_url="../../ecoles/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urls']=['/dashboard/curcus/', '/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Ecole creer avec succes.')
      return super().form_valid(form)
class UpdateSchool(UpdateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = School
   form_class=SchoolForm
   template_name="school/update-school.html"
   success_url="../../ecoles/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urls']=['/dashboard/curcus/','/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Ecole modifier avec succes')
      return super().form_valid(form)
class DeleteSchool(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = School
   template_name = "school/delete-school.html"
   success_url="../../ecoles/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages=messages.success(self.request, "L'ecole a été supprimé avec succès")
      reponses = [response,messages]
      return reponses

class ListCurcus(ListView,LoginRequiredMixin, SuperuserRequiredMixin):
    model = Curriculum
    context_object_name = 'curcus'
    paginate_by = 10
    template_name = "school/curcus/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urls']=['/dashboard/curcus/', '/dashboard/ecole/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      # context['urlsA']=['']
      return context
class CreateCursus(CreateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Curriculum
   form_class=CurcusForm
   template_name="school/curcus/create-curcus.html"
   success_url="../../curcus/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urls']=['/dashboard/curcus/','/dashboard/cursus/create/', '/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Cursus creer avec succes.')
      return super().form_valid(form)
class UpdateCursus(UpdateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Curriculum
   form_class=CurcusForm
   template_name="school/curcus/update-curcus.html"
   success_url="../../curcus/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urls']=['/dashboard/curcus/','/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'cursus modifier avec succes')
      return super().form_valid(form)
class DeleteCursus(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Curriculum
   template_name = "school/curcus/delete-cursus.html"
   success_url="../../curcus/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages=messages.success(self.request, "Le curcus a été supprimé avec succès")
      reponses = [response,messages]
      return reponses

class ListLevel(ListView,LoginRequiredMixin, SuperuserRequiredMixin):
    model = Level
    context_object_name = 'levels'
    paginate_by = 10
    template_name = "school/niveaux/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urls']=['/dashboard/curcus/', '/dashboard/ecole/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      # context['urlsA']=['']
      return context
class CreateLevel(CreateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Level
   form_class=LevelForm
   template_name="school/niveaux/create-niveau.html"
   success_url="../../niveau/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urls']=['/dashboard/curcus/','/dashboard/niveaux/create/', '/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Niveau creer avec succes.')
      return super().form_valid(form)
class UpdateLevel(UpdateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Level
   form_class=LevelForm
   template_name="school/niveaux/update-niveau.html"
   success_url="../../niveau/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urls']=['/dashboard/curcus/','/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Niveau modifier avec succes')
      return super().form_valid(form)
class DeleteLevel(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin ): 
   model = Level
   template_name = "school/niveaux/delete-niveau.html"
   success_url="../../niveau/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages=messages.success(self.request, "Le niveau a été supprimé avec succès")
      reponses = [response,messages]
      return reponses
   
class ListStream(ListView,LoginRequiredMixin, SuperuserRequiredMixin):
    model = Stream
    context_object_name = 'filieres'
    paginate_by = 10
    template_name = "school/filiere/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urls']=['/dashboard/curcus/', '/dashboard/ecole/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      # context['urlsA']=['']
      return context
class CreateStream(CreateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Stream
   form_class=StreamForm
   template_name="school/filiere/create-filiere.html"
   success_url="../../filiere/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urls']=['/dashboard/curcus/','/dashboard/filieres/create/', '/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Filiere creer avec succes.')
      return super().form_valid(form)
class UpdateStream(UpdateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Stream
   form_class=StreamForm
   template_name="school/filiere/update-filiere.html"
   success_url="../../filiere/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urls']=['/dashboard/curcus/','/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'filiere modifier avec succes')
      return super().form_valid(form)
class DeleteStream(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin):  
   model = Stream
   template_name = "school/filiere/delete-filiere.html"
   success_url="../../filiere/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages=messages.success(self.request, "La filiere a été supprimé avec succès")
      reponses = [response,messages]
      return reponses

class ListTest(ListView,LoginRequiredMixin, SuperuserRequiredMixin):
    model = Test
    context_object_name = 'epreuves'
    paginate_by = 10
    template_name = "school/epreuves/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urls']=['/dashboard/curcus/', '/dashboard/ecole/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      # context['urlsA']=['']
      return context
class CreateTest(CreateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Test
   form_class=TestForm
   template_name="school/epreuves/create-epreuve.html"
   success_url="../../epreuve/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urls']=['/dashboard/curcus/','/dashboard/epreuves/create/', '/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Epreuve creer avec succes.')
      return super().form_valid(form)
class UpdateTest(UpdateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Test
   form_class=TestForm
   template_name="school/epreuves/update-epreuve.html"
   success_url="../../epreuve/"

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urls']=['/dashboard/curcus/','/dashboard/ecoles/','/dashboard/niveau/','/dashboard/filiere/','/dashboard/epreuve/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Epreuve modifier avec succes')
      return super().form_valid(form)
class DeleteTest(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin):  
   model = Level
   template_name = "school/epreuves/delete-epreuve.html"
   success_url="../../epreuve/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages=messages.success(self.request, "L'epreuve' a été supprimé avec succès")
      reponses = [response,messages]
      return reponses
 

'''manipulation des abonnement'''
class ListPack(ListView,LoginRequiredMixin, SuperuserRequiredMixin,School):
    model = Pack
    context_object_name = 'abonnements'
    paginate_by = 10
    template_name = "abonnements/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsA']=['/dashboard/abonnement/']
      return context   
class CreatePack(CreateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Pack
   form_class=PackForm
   template_name="abonnements/add-pack.html"
   success_url="../../abonnement/"
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsA']=['/dashboard/abonnement/','/dashboard/abonnement/create/']
      return context
class UpdatePack(UpdateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Pack
   form_class=PackForm
   template_name="abonnements/update-pack.html"
   success_url="../../abonnement/"
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsA']=['/dashboard/abonnement/','/dashboard/abonnement/create/','/dashboard/abonnement/update/',
                        '/dashboard/abonnement/update/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Pack modifier avec succes')
      return super().form_valid(form)
class DeletePack(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Pack
   template_name = "abonnements/delete-pack.html"
   success_url="../../abonnement/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages.success(self.request, 'Le pack a été supprimé avec succès.')
      return response

'''manipulation des cours'''
class ListCours(ListView,LoginRequiredMixin, SuperuserRequiredMixin):
    model = Cours
    context_object_name = 'cours'
    paginate_by = 10
    template_name = "cours/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsC']=['/dashboard/cours/']
      return context    
class CreateCours(CreateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Cours
   form_class=CoursForm
   template_name="cours/add-cour.html"
   success_url="../../cours/"
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsC']=['/dashboard/cours/','/dashboard/cours/create/']
      return context
   
   def form_valid(self, form):
      name = form.cleaned_data.get('name')
      if Cours.objects.filter(name=name).exists():
         form.add_error('name', 'Ce cour existe deja.')
         return self.form_invalid(form)
      else:
         messages.success(self.request, 'cour creer avec succes')
         return super().form_valid(form)
class UpdateCours(UpdateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Cours
   form_class=CoursForm
   template_name="cours/update-cour.html"
   success_url="../../cours/"
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsC']=['/dashboard/cours/','/dashboard/cours/create/']
      return context
   def form_valid(self, form):
      messages.success(self.request, 'Cour modifier avec succes')
      return super().form_valid(form)
class DeleteCours(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Cours
   template_name = "cours/delete-cour.html"
   success_url="../../cours/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages.success(self.request, 'Le cours a été supprimé avec succès')
      return response

'''gestion du blog'''
class ListCatagory(ListView,LoginRequiredMixin, SuperuserRequiredMixin):
    model = Category
    context_object_name = 'category'
    paginate_by = 10
    template_name = "blog/categories/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urlsB']=['/dashboard/blog/categorie/','/dashboard/blog/categorie/create/']
      return context
class CreateCategory(CreateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Category
   form_class=CategoryForm
   template_name="blog/categories/create.html"
   success_url="../../categorie/"
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsB']=['/dashboard/blog/categorie/','/dashboard/blog/categorie/create/']
      return context
   def form_valid(self, form):
      name = form.cleaned_data.get('name')
      if Category.objects.filter(name=name).exists():
         form.add_error('name', 'Cette categorie existe deja.')
         return self.form_invalid(form)
      else:
         messages.success(self.request, 'Categorie creer avec succes.')
         return super().form_valid(form)
class UpdateCategory(UpdateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Category
   form_class=CategoryForm
   template_name="blog/categories/update-categori.html"
   success_url="../../../categorie/"
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsB']=['/dashboard/blog/categorie/','/dashboard/blog/categorie/create/']
      return context  
   def form_valid(self, form):
      messages.success(self.request, 'Categorie modifier avec succes')
      return super().form_valid(form)
class DeleteCategory(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Category
   template_name = 'blog/categories/delete.html'
   success_url = success_url="../../../categorie/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages.success(self.request, 'La categorie a été supprimé avec succès.')
      return response

class ListArticle(ListView,LoginRequiredMixin, SuperuserRequiredMixin):
    model = Article
    context_object_name = 'articles'
    paginate_by = 10
    template_name = "blog/articles/list.html"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urlsB']=['/dashboard/blog/categorie/','/dashboard/blog/categorie/create/','/dashboard/blog/article/','/dashboard/blog/create/']
      return context
class CreateArticle(CreateView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Article
   form_class = ArticleForm
   template_name = "blog/articles/create.html/"
   success_url="../../article/"
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsB']=['/dashboard/blog/categorie/','/dashboard/blog/categorie/create/','/dashboard/blog/article/create/','/dashboard/blog/article/']
      return context
   def form_valid(self, form):
      titre = form.cleaned_data.get('titre')
      if Article.objects.filter(titre=titre).exists():
         form.add_error('titre', 'Cette article existe deja.')
         return self.form_invalid(form)
      else:
         messages.success(self.request, 'Article creer avec succes.')
         return super().form_valid(form)
class UpdateArticle(UpdateView,LoginRequiredMixin, SuperuserRequiredMixin):
    model=Article
    form_class=ArticleForm
    template_name="blog/articles/update.html"
    success_url="../../../article/"
   
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      context['urlsB']=['/dashboard/blog/categorie/','/dashboard/blog/categorie/create/','/dashboard/blog/article/update/','/dashboard/blog/article/']
      return context  
    def form_valid(self, form):
      messages.success(self.request, 'Article modifier avec succes')
      return super().form_valid(form)
class DeleteArticle(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Article
   template_name = "blog/articles/delete.html"
   success_url="../../../article/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages.success(self.request, 'La categorie a été supprimé avec succès.')
      return response

'''gestion des utilisateurs admin'''
class ListUSer( SuperuserRequiredMixin,ListView,LoginRequiredMixin,):
   model=User
   context_object_name = 'users'
   paginate_by = 10
   template_name = "users/list-user.html"
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      return context   

'''subscription'''
# Vue baser sur les classes
'''gestion des messages'''
class ListMessage(ListView,LoginRequiredMixin, SuperuserRequiredMixin):
   model=Message
   context_object_name = 'messages'
   paginate_by = 10
   template_name = "message/list.html"
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['current_url'] = self.request.path
      # context['urls']=['']
      context['urlsC']=['/dashboard/cours/','/dashboard/messages/']
      return context  
    
class DeleteMessage(DeleteView,LoginRequiredMixin, SuperuserRequiredMixin):
   model = Message
   template_name = "message/message-delete.html"
   success_url="../../messages/"

   def delete(self, request, *args, **kwargs):
      response = super().delete(request, *args, **kwargs)
      messages.success(self.request, 'La message a été supprimé avec succès.')
      return response
   
def mark_message_as_read(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.is_read = True
    message.save()
    return redirect('message.list')

def message_reponse(request, message_id):
   message=get_object_or_404(Message, id=message_id)
   message.is_read = True
   message.save()
   current_url = request.get_full_path()
   if request.method == 'POST':
      form = ReponseForm(request.POST,instance=message)
      if form.is_valid():
         response = form.cleaned_data['response']
         form.save()
         messages.success(request, 'Votre reponse a ete envoyer succès.')
         send_mail(
                'Réponse à votre message',
                f'Vous: {message.Message}\n\nelitecorp.org: {response}',  
                settings.DEFAULT_FROM_EMAIL,# From email
                [message.email],  # To email
                fail_silently=False,
            )
         return redirect('message.list')   
      else :
         context ={
         'current_url':current_url,
         'message':message,
         'form':form,
          }
         for field in form.errors:
            print(field)
         return render(request, 'message/reponse-message.html', context)
   else:
      form = ReponseForm()
      context ={
            'current_url':current_url,
            'message':message,
            'form':form,
         }
      return render(request, 'message/reponse-message.html', context)