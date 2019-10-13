from django.contrib.auth.signals import user_logged_out, user_logged_in, user_login_failed
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    #model = User
    messages.add_message(request, messages.WARNING, 'Ha cerrado sesión')
    #obj = self.get_object()
    #SuccessMessageMixin.success_message = "%(user)s ha cerrado sesión"

    #obj = self.get_object()
    #messages.success(self.request, self.success_message % obj.__dict__)

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    messages.add_message(request, messages.SUCCESS, 'Ha iniciado sesión')

@receiver(user_login_failed)
def on_user_login_failed(sender, request, **kwargs):
    messages.add_message(request, messages.ERROR, 'Usuario o contraseña incorrecta')



