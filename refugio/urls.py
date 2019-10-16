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
from django.contrib.auth import urls
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
#password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascota/', include ('apps.mascota.urls'), name='mascota'),
    path('adopcion/', include ('apps.adopcion.urls'), name='adopcion'),
    path('solicitud/', include ('apps.adopcion.urls'), name='solicitud'),
    path('usuario/', include ('apps.usuario.urls'), name='usuario'),
    #url(r'^registrar$', RegistroUsuario.as_view(), name='registrar'),
    #path('usuario/', include('django.contrib.auth.urls')), #TODAS LAS URL
    #path('logout/', LogoutView.as_view(template_name='usuario/login.html'), name='logout'),
    path('logout/', logout_then_login, name='logout'),
    path('accounts/login/', LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'), #, 'email_template_name':'registration/password_reset_email.html'
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('api-auth/', include('rest_framework.urls')),

    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
]

urlpatterns += staticfiles_urlpatterns()

#path('', login, {'template_name':'index.html'}, name='login'),
#path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),



    #path('logout/', logout_then_login, name='logout'),
    #path('accounts/login/', LoginView.as_view(template_name='usuario/index.html'), name='login'),
    #path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'), #, 'email_template_name':'registration/password_reset_email.html'
    #path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    #path('reset/done', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
