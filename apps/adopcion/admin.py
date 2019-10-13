from django.contrib import admin

from apps.adopcion.models import Persona, Solicitud

# Register your models here.
admin.site.register(Solicitud)
admin.site.register(Persona)

