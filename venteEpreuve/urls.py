from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("front.urls")),
    path('blog/', include("blog.urls")),
    path('',include("auth_app.urls")),
    path("dashboard/", include("admin_site.urls")),
    path("cours/", include("cours.urls")),
    path("epreuve/", include("ecole.urls")),
    path("abonnement/",include('abonnement.urls')),
    path("j-m-abonne/",include('panier.urls')),
    path('larue/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('contact/', include('contact.urls')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
