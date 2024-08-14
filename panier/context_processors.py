from .models import Cart, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required

def cart_item_count(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            item_count = cart.items.count()
            total_price = cart.get_total_price()
        except Cart.DoesNotExist:
            item_count = 00
            total_price = 0
    else:
        item_count = 00
        total_price = 0
    return {'cart_item_count': item_count,
            'cart_total_price': total_price,}

