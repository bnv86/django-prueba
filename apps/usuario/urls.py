from django.conf.urls import url, include
from apps.usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar$', RegistroUsuario.as_view(), name='registrar'),

]

    #url(r'^listar$', SolicitudList.as_view(), name='solicitud_listar'),
    #url(r'^nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),
"""     url(r'^editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='solicitud_eliminar'), """