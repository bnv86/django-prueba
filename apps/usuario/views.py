import json
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #PasswordChangeForm, UserChangeForm
#from registration.signals import user_registered
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DetailView, View
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy, reverse
from apps.usuario.forms import RegistroForm, UserEditForm, profileForm
#from .models import UserProfile
from django.core import serializers
from apps.usuario.serializer import UserSerializer
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
#from django.contrib.auth.signals import user_logged_out
#from django.dispatch import receiver

# Create your views here.

# Serializado para la API
def listado(request):
    lista = serializers.serialize('json', User.objects.all(), fields=['username', 'email', 'first_name', 'last_name'])
    return HttpResponse(lista, content_type='application/json')

class UsuarioRegister(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm #UserCreationForm
    success_url = reverse_lazy('login')
    # en algun momento tengo que cambiar esto, para que primero envie un mail de confirmacion como en password_reset
    success_message = "%(username)s ha sido registrado con éxito!"

"""
class UsuarioUpdate(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'usuario/perfil.html'
    form_class = UserEditForm #UserChangeForm
    success_url = reverse_lazy('solicitud_listar')
    # en algun momento tengo que cambiar esto, para que primero envie un mail de confirmacion como en password_reset
    success_message = "%(username)s ha sido modificado con éxito!"
"""


"""
class UpdateUserView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'usuario/perfil.html'
    success_url = reverse_lazy('solicitud_listar')
"""

@login_required
def profileUpdate(request):
    """
    if request.method == 'POST':
        form = profileForm(data=request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('somewhere')
    
    if request.method == 'POST':
        form = profileForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
    else:
        form = profileForm(instance=request.user)

    return render(request, 'usuario/profile.html', {'form': form})
    """

    #usuario = User.objects.get(id=id_user)
    if request.method == 'GET':
        form = profileForm(instance=request.user)
    else:
        form = profileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        #SuccessMessageMixin.success_message = "%(username)s ha sido modificado con éxito!"
        messages.add_message(request, messages.SUCCESS, 'Ha modificado el perfil correctamente')
        return redirect('solicitud_listar')
    return render(request, 'usuario/profile_update.html', {'form':form})

"""
class UsuarioDetail(View):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        context = {'user': user}
        return render(request, 'usuario/profile_detail.html', context)
"""

#class UsuarioDetail(DetailView):

    #queryset = User.objects.all()

    #def get_object(self):
        #obj = super().get_object()
        # Record the last accessed date
        #obj.last_accessed = timezone.now()
        #obj.save()
        #return obj

    #model = User
    #user_ide = User.objects.get(id=user_id)
    #queryset = Book.objects.filter(is_published=True)
    #form = profileForm(instance=model.id)
    #template_name = 'usuario/profile_detail.html'
    #success_url = reverse_lazy('solicitud_listar')
    #def get_success_url(self):
        #return reverse_lazy('facture_consulter',kwargs={'pk': self.get_object().id})
        #print('ID: '+ self.get_object().id)
        #return get_object_or_404(User, kwargs={'pk': self.get_object().id})
    
    #def get_object(self):
        #return get_object_or_404(User, pk=session['user_id'])
        #return get_object_or_404(User, kwargs={'pk': self.get_object().id})
    
    #def get_object(self):

        #return get_object_or_404(User, pk=self.get_object().id)

    #def get_queryset(self):
    		#if self.request.user.is_authenticated:
			    #return self.get_object().id


#falta que tome el user id para que funcione
class UsuarioUpdate(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserEditForm
    #form = profileForm(instance=model.id)
    template_name = 'usuario/profile.html'
    success_url = reverse_lazy('solicitud_listar')
    success_message = "%(username)s ha sido modificado con éxito!"


#implementar en urls globales y en logout.html
class LogoutUsuario(SuccessMessageMixin, LogoutView):
    model = User
    #form_class = MascotaForm
    #template_name = 'mascota/delete.html'
    success_url = reverse_lazy('login')
    success_message = "%(username)s ha cerrado sesión!"


class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')









"""
@login_required
def EditUser(request, slug=None):

    #Editar usuario de forma simple.

    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            #Actualizar el objeto
            user = form.save()
            messages.success(request, 'Usuario actualizado exitosamente.', extra_tags='html_dante')
            return HttpResponseRedirect(reverse('solicitud_listar'))
    else:
        form = UserChangeForm(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'home/user_change.html', context)
"""

"""
class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home:login_user'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class EditUser(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'home/user_change.html'
    slug_url_kwarg = 'empleado_slug'

    def get_success_url(self):
        return reverse('solicitud_listar')

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(EditUser, self).dispatch(*args, **kwargs)


def asegurar_existencia_perfil_user(pk):
    usuario = User.objects.get(pk=pk)
    try:
        userprofile = usuario.userprofile
    except (UserProfile.DoesNotExist, e):
        userprofile = UserProfile(user=usuario)
        userprofile.save()
    return userprofile


@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='usuario/password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    empleado_slug=None,
                    extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('accounts/login')
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one if
            # django.contrib.auth.middleware.SessionAuthenticationMiddleware
            # is enabled.
            messages.success(request, _('Contrasena cambiado correctamente'),extra_tags='html_dante')
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': _('Password change'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)

class EditUserProfile(LoginRequiredMixin,UpdateView):
    model = UserProfile
    template_name = 'usuario/form_userprofile.html'
    fields = ['first_name', 'last_name', 'username']
    slug_url_kwarg = 'profile_slug'
    # pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        asegurar_existencia_perfil_user(self.kwargs['pk'])
        return (super(EditUserProfile, self).get(self, request, *args, **kwargs))

class DetailUserProfile(LoginRequiredMixin,DetailView):
    model = UserProfile
    # slug_url_kwarg = 'profile_slug'
    template_name = 'usuario/detail_userprofile.html'

"""