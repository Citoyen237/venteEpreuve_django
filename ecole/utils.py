from django.utils import timezone
from abonnement.models import Pack as Product

def get_expired_products():
    today = timezone.now().date()
    expired_products = []

    products = Product.objects.all()
    for product in products:
        expiration_date = product.expiration_date.date()
        if expiration_date <= today:
            expired_products.append(product)

    return expired_products
