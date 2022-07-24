from django.shortcuts import render
from django.views import View

from .forms import SignUpForm,LoginForm,UpdatePasswordForm
from django.views.generic import(
    FormView,
    View,
) 

from .models import User
from django.urls import reverse_lazy , reverse

from django.contrib.auth import authenticate, login,logout

from django.http import HttpResponseRedirect

class UserRegisterViewView(FormView):
    template_name = 'users/signup.html'
    form_class=  SignUpForm
    success_url = '/'

    def form_valid(self, form):

        User.objects.create_user( #use el manager que cree
            form.cleaned_data['username'], #recupero del formulario el username
            
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            email=form.cleaned_data['email'],
            password = form.cleaned_data['password1'],
            genero = form.cleaned_data['genero'], #extra fields
        ) 

        return super(UserRegisterViewView,self).form_valid(form)

class UserLogin(FormView):
    template_name = 'users/login.html'
    form_class=  LoginForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):

        # validation of user
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
        )

        # if validated user can login
        login(self.request, user)

        return super(UserLogin,self).form_valid(form)

class logoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request) 
        return HttpResponseRedirect(
            reverse(
                'home:HomePage'
            )

        )

class UpdatePassword(FormView):
    template_name = 'users/updatePassword.html'
    form_class=  UpdatePasswordForm
    success_url = reverse_lazy('users_app:login')

    def form_valid(self, form):

        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1'],
        )
        #if authenticated 
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password) #encripta contraseña con set_password
        logout(self.request) #cuando actualiza pide que vuelva a ingresar con nueva contraseña

        return super(UpdatePassword,self).form_valid(form)