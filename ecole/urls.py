from django.urls import path
from.views import *

urlpatterns = [
    path('',index, name='index.ecole'),
    path('schools/<int:school_id>',schoolTest,name='school.test'),
    path('niveaux/<int:niveau_id>',schoolLevelTest,name='school.niveau.test'),
    path('cursus/<int:cursus_id>',schoolCirrulumTest,name='school.cursus.test'),
    path('filieres/<int:filiere_id>',schoolLevelFiliere,name='school.niveau.tream.test'),
    path('stream/<int:level_id>',schoolCursusLevelTest,name='school.cursus.level.test'),
    path('ecole/<int:level_id>',schoolCursusLevelFiliere,name='school.cursus.niveau.tream.test'),
    path('telecharge-epreuve/<int:test_id>',get_download_test ,name='download.test')
]
