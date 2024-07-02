from django.urls import path
from .views import *

urlpatterns = [
    path('ajouter-au-panier/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('panier/', view_cart, name='cart'),
    path('paiement/', checkout, name='checkout'),
    path('detail-de-la-commande/<int:order_id>/', order_detail, name='order_detail'),
    path('panier/delete/<int:item_id>/', delete_cart_item, name='delete_item'),

]