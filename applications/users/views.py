from django.shortcuts import render

from .forms import SignUpForm
from django.views.generic import(
    CreateView
) 

class UserRegisterViewCreateView(CreateView):
    template_name = 'users/signup.html'
    form_class=  SignUpForm
    success_url = '/'
