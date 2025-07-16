"""
URL configuration for Agencia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from ClientePOV import views
from django.conf.urls.static import static 


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('sejaModelo', views.sejaModelo, name='sejaModelo'),
    path('Equipe', views.Equipe, name='Equipe'), 
    path('analisando', views.analisando, name="analisando"),
    
    
    path('produtores/', include('produtores.urls')),
    path('fotografos/', include('fotografos.urls')),
    path('CEO/', include('CEO.urls')),
    path('cabeleireiros/', include('cabeleireiros.urls')),
    path('estilistas/', include('estilistas.urls')),
    path('maquiadores/', include('maquiadores.urls')),
    path('modelos/', include('modelos.urls')),
    path('adminauth/', include('auxiliarAdmPOV.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
