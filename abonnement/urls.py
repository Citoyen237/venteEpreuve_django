from django.urls import path
from .views import *

urlpatterns = [
    path('',ListAbonnement.as_view(), name='abonnement.index'),
    path('detail-sur-abonnement/<int:pack_id>',detailAbonnement, name='abonnement.detail'),
    path('mes-abonnements/', get_abonnement_user,name='abonnement.user')
]
