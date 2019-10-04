"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('mascota/', include ('apps.mascota.urls', namespace="mascota")),
    #path('adopcion/', include ('apps.adopcion.urls', namespace="adopcion")),
    path('mascota/', include ('apps.mascota.urls'), name='mascota'),
    path('adopcion/', include ('apps.adopcion.urls'), name='adopcion'),
    path('solicitud/', include ('apps.adopcion.urls'), name='solicitud'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
]

urlpatterns += staticfiles_urlpatterns()

