from django.conf.urls import url, include
from apps.mascota.views import index_mascota, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
from django.views.generic import TemplateView

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', index_mascota, name='index_mascota'),
    #vistas basadas en clases
    url(r'^nueva$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^listar$', MascotaList.as_view(), name='mascota_listar'),
    url(r'^editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),

    #vistas basadas en funciones
    #url(r'^listar$', mascota_list, name='mascota_listar'),
    #url(r'^nuevo$', mascota_view, name='mascota_crear'),
    #url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    #url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),

    #url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
]
