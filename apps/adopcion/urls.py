from django.conf.urls import url, include
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate

urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^index$', index_adopcion),
    url(r'^$', index_adopcion, name='index_adopcion'),
    url(r'^listar$', SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),

]
