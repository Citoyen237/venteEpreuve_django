from django.shortcuts import render
from blog.models import Article

# Create your views here.
def index(request): 
    articles = Article.objects.order_by('-created_at')[:4]
    current_url = request.get_full_path()
    context = {
        'articles':articles,
        'current_url':current_url,
    }
    return render(request, 'index.html',context)

def pagenotfound(request):
    return render(request, 'page404.html')