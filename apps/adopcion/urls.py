from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete, \
    ListSolicitud, ListPersona, listadoPersona, listadoSolicitud

urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^index$', index_adopcion),
    url(r'^$', login_required(index_adopcion), name='index_adopcion'),
    url(r'^listar', login_required(SolicitudList.as_view()), name='solicitud_listar'),
    url(r'^nueva$', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),

    #API
    url(r'^listadoPersona$', login_required(listadoPersona), name='listado_persona'),
    url(r'^listadoSolicitud$', login_required(listadoSolicitud), name='listado_solicitud'),

    #api en uso
    url(r'^api/solicitudes/$', ListSolicitud.as_view(), name='solicitud_api'),
    url(r'^api/personas/$', ListPersona.as_view(), name='personas_api'),
]
