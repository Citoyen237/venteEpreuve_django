from .models import Article

def articles_context_processor(request):
    articless = Article.objects.order_by('-created_at')[:5]
    return {'articless': articless}