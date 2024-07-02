from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('creer-un-compte/',registerPage, name='auth.register'),
    path('connexion/',loginPage, name='auth.login'),
    path('renitialiser-le-mot-de-passe/', forgetPassPage, name='auth.forgetPass'),
    path('se-deconnecter/', logoutPage, name='auth.logout'),
]
