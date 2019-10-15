from django.conf.urls import url, include
from apps.usuario.views import listado, UsuarioRegister, UsuarioUpdate, UsuarioDetail, UserAPI, profileUpdate #, EditUserProfile, DetailUserProfile, EditUser, password_change, UpdateUserView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    url(r'^registrar$', UsuarioRegister.as_view(), name='registrar'),
    #url(r'^editar/(?P<pk>\d+)$', UsuarioUpdate.as_view(), name='perfil'),

    url(r'^listado', login_required(listado), name='listado'),
    url(r'^api$', UserAPI.as_view(), name='api'),

    url(r'^detail/<int:pk>/$', login_required(UsuarioDetail.as_view()), name='profile_detail'),
    url(r'^update$', login_required(views.profileUpdate), name='profile_update'),
    #url(r'^profile/(?P<pk>\d+)$', login_required(UsuarioUpdate.as_view()), name='profile'),

    #url(r'^<int:pk>/', UpdateUserView.as_view(), name='users-edit'),           (r'^(?P<id>\d+)'
    
]

    #url(r'^listar$', SolicitudList.as_view(), name='solicitud_listar'),
    #url(r'^nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),
""" url(r'^editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='solicitud_eliminar'), 
    
    #Cambiar Usuario creado
    # url(r'^usuario/(?P<pk>[0-9]+)/editar/$', views.EditUser,
    #     name="editar_user"),
    url(r'^usuario/(?P<empleado_slug>[\w-]+)/editar/$', views.EditUser.as_view(),
        name="editar_user"),

    # Cambiar Contraseña de usuario
    # url(r'^usuarios/', include('django.contrib.auth.urls')),
    url(r'^usuario/(?P<empleado_slug>[\w-]+)/password_change/$', views.password_change,
        name="password_change"),

    ## Gestion de perfiles de usuarios
    url(r'^usuario/(?P<pk>[0-9]+)/perfil/editar/$', views.EditUserProfile.as_view(), name='editar_userprofile'),
    url(r'^usuario/(?P<pk>[0-9]+)/perfil/(?P<profile_slug>[\w-]+)/$', views.DetailUserProfile.as_view(), name='detalle_userprofile'),
    
    
    #PRUEBAS
    url(r'^(?P<pk>[0-9]+)/perfil/editar/$', EditUserProfile.as_view(), name='editar_userprofile'),
    url(r'^(?P<pk>[0-9]+)/perfil/(?P<profile_slug>[\w-]+)/$', DetailUserProfile.as_view(), name='detalle_userprofile'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^(?P<user_slug>[\w-]+)/password_change/$', password_change,
        name="password_change"),
        
    url(r'^(?P<user_slug>[\w-]+)/editar/$', EditUser.as_view(),
        name="editar_user"),
    """