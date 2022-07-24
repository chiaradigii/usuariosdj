from tkinter.tix import Tree
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate
# from django.utils.translation import ugettext, ugettext_lazy as _

class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir ontraseña'
            }
        )
    )

    class Meta:
        """Meta definition for UserForm"""
        model = User
        fields=(
            'username',
            'email',
            'nombre',
            'apellido',
            'genero',
            'password1',
            'password2',
            )



    def clean_password1(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = self.cleaned_data['password1']

        # check for min length
        if len(password) < 8:
            self.add_error('password1','La contraseña requiere al menos 8 caracteres')
        # check for char
        if not any(char.isalpha() for char in password):
            self.add_error('password1','La contraseña debe contener letras')
        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password1', msg)
        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password1', msg)
        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password1', msg)

        password_confirm = cleaned_data.get('password2')

        if password and password_confirm:
            if password != password_confirm:
                msg = "Las contraseñas deben coincidir."
                self.add_error('password2', msg)



class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    
    #validation
    def clean(self):
        self.cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Los datos no son correctos')
        return self.cleaned_data

class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Nueva contraseña'
            }
        )
    )