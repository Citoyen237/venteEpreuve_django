from django.urls import path
from .views import *

urlpatterns = [
    path('', indexAdmin ,name='dashboard.index'),
    
    path('ecoles/',ListSchool.as_view(),name='ecole.list'),
    path('ecoles/create/',CreateSchool.as_view(),name='ecole.create'),
    path('ecoles/update/<int:pk>',UpdateSchool.as_view(),name='ecole.update'),
    path('ecoles/delete/<int:pk>',DeleteSchool.as_view(),name='ecole.delete'),

    path('curcus/',ListCurcus.as_view(),name='curcus.list'),
    path('cursus/create/',CreateCursus.as_view(),name='cursus.create'),
    path('cursus/update/<int:pk>',UpdateCursus.as_view(),name='cursus.update'),
    path('cursus/delete/<int:pk>',DeleteCursus.as_view(),name='cursus.delete'),
    
    path('niveau/',ListLevel.as_view(),name='niveau.list'),
    path('niveaux/create/',CreateLevel.as_view(),name='niveau.create'),
    path('niveaux/update/<int:pk>',UpdateLevel.as_view(),name='niveau.update'),
    path('niveaux/delete/<int:pk>',DeleteLevel.as_view(),name='niveau.delete'),

    path('filiere/',ListStream.as_view(),name='filiere.list'),
    path('filieres/create/',CreateStream.as_view(),name='filiere.create'),
    path('filieres/update/<int:pk>',UpdateStream.as_view(),name='filiere.update'),
    path('filieres/delete/<int:pk>',DeleteStream.as_view(),name='filiere.delete'),

    path('epreuve/',ListTest.as_view(),name='epreuve.list'),
    path('Epreuves/create/',CreateTest.as_view(),name='epreuve.create'),
    path('Epreuves/update/<int:pk>',UpdateTest.as_view(),name='epreuve.update'),
    path('Epreuves/delete/<int:pk>',DeleteTest.as_view(),name='epreuve.delete'),

    path('abonnement/', ListPack.as_view(), name='pack.list'),
    path('abonnement/create/', CreatePack.as_view(), name='pack.create'),
    path('abonnement/update/<int:pk>', UpdatePack.as_view(), name='pack.update'),
    path('abonnement/delete/<int:pk>', DeletePack.as_view(), name='pack.delete'),

    path('cours/', ListCours.as_view(), name='cours.list'),
    path('cours/create/', CreateCours.as_view(), name='cours.create'),
    path('cours/update/<int:pk>', UpdateCours.as_view(), name='cours.update'),
    path('cours/delete/<int:pk>', DeleteCours.as_view(), name='cours.delete'),
    
    path('messages/', ListMessage.as_view(), name='message.list'),
    path('messages/delete/<int:pk>', DeleteMessage.as_view(), name='message.delete'),
    path('messages/mark-read/<int:message_id>', mark_message_as_read, name='message.read'),
    path('messages/reponse/<int:message_id>', message_reponse, name='message.reponse'),


    path('blog/categorie/',ListCatagory.as_view(), name='category.list'),
    path('blog/categorie/creeate/',CreateCategory.as_view(), name='category.create'),
    path('blog/categorie/update/<int:pk>/',UpdateCategory.as_view(), name='category.create'),
    path('blog/categorie/delete/<int:pk>/', DeleteCategory.as_view(), name='category.delete'),

    path('blog/article/',ListArticle.as_view(), name='article.list'),
    path('blog/article/create/',CreateArticle.as_view(), name='article.create'),
    path('blog/article/update/<int:pk>/',UpdateArticle.as_view(), name='article.update'),
    path('blog/article/delete/<int:pk>/', DeleteArticle.as_view(), name='article.delete'),

    path('utilisateurs/',ListUSer.as_view(), name='user.list'),
]

