from django.conf.urls import url, include
from apps.adopcion.views import index_adopcion

urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^index$', index_adopcion),
    url(r'^$', index_adopcion),
]
