from django.conf.urls import url, include
from apps.mascota.views import index_mascota, mascota_view, mascota_list
from django.views.generic import TemplateView

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', index_mascota, name='index_mascota'),
    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^listar$', mascota_list, name='mascota_listar'),
    #url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
]
