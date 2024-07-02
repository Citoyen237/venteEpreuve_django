from django.shortcuts import render,get_object_or_404
from .models import Article, Category
from django.db.models import Count
from django.http import HttpResponse

# Create your views here.
def ArticleDetail(request,article_id):
    '''compter le nombre article que contient une categorie'''
    categories = Category.objects.annotate(num_articles=Count('article'))
    article = get_object_or_404(Article, id=article_id)
    articles = Article.objects.order_by('-created_at')[:3]
    context ={
        'article': article,
        'categories':categories,
        'articles':articles,
    }
    return render(request, 'detail_blog.html',context)

def CartegoriArticle(request, categorie_id):
    categories = Category.objects.annotate(num_articles=Count('article'))
    articless = Article.objects.filter(category=categorie_id)
    articles = Article.objects.order_by('-created_at')[:3]
    context ={
        'articless': articless,
        'categories':categories,
        'articles':articles,
    }
    return render(request, 'article-categorie.html',context)

def CartegoriArticle(request, categorie_id):
    categories = Category.objects.annotate(num_articles=Count('article'))
    articless = Article.objects.filter(category=categorie_id)
    articles = Article.objects.order_by('-created_at')[:3]
    context ={
        'articless': articless,
        'categories':categories,
        'articles':articles,
    }
    return render(request, 'article-categorie.html',context)

def ListArticles(request):
    categories = Category.objects.annotate(num_articles=Count('article'))
    articless = Article.objects.order_by('-created_at')
    articles = Article.objects.order_by('-created_at')[:3]
    current_url = request.get_full_path()
    context ={
        'articless': articless,
        'categories':categories,
        'articles':articles,
        'current_url':current_url,
    }
    return render(request, 'articles.html',context)

def download_file(request, file_id):
    document = get_object_or_404(Article, id=file_id)
    response = HttpResponse(document.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response