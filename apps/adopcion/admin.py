from django.contrib import admin
from django.contrib.auth.models import User

from apps.adopcion.models import Persona, Solicitud

# Register your models here.

class SolicitudAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'username':
            kwargs['queryset'] = User.objects.filter(username=request.user.username)
        return super(SolicitudAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('username',)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['username'] = request.user
        request.GET = data
        return super(SolicitudAdmin, self).add_view(request, form_url="", extra_context=extra_context)

admin.site.register(Solicitud)
admin.site.register(Persona)

