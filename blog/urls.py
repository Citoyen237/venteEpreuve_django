from django.urls import path
from .views import *

urlpatterns = [
    path("", ListArticles, name="articles"),
    path('voir-plus/<int:article_id>', ArticleDetail, name='article.detail'),
    path('categories/<int:categorie_id>', CartegoriArticle, name='categorie.article'),
    path('download-article/<int:article_id>/', download_file, name='download_article'),
]
