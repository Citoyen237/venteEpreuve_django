from django.shortcuts import render
from blog.models import Article
from .models import Cours
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Create your views here.
def apprentissage(request):
    articles = Article.objects.order_by('-created_at')[:4]
    current_url = request.get_full_path()
    context = {
        'articles':articles,
        'current_url':current_url,
    }
    return render(request, 'apprentissage.html',context)

def cours(request):
    cours = Cours.objects.order_by('-created_at')[:4]
    current_url = request.get_full_path()
    context = {
        'cours':cours,
        'current_url':current_url,
    }
    return render(request, 'cours.html',context)

def download_file(request, file_id):
    document = get_object_or_404(Cours, id=file_id)
    response = HttpResponse(document.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response