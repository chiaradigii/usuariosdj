from django import forms
from .models import User

class SignUpForm(forms.ModelForm):

    class Meta:
        """Meta definition for UserForm"""
        model = User
        fields=('__all__')