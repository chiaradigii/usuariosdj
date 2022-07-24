from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy , reverse

from django.views.generic import (
    TemplateView
)

#does not require login
class HomePage(TemplateView):
    template_name = "home/home.html"

#require login
class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "home/index.html"
    login_url= reverse_lazy('users_app:login') #if not authenticated, go to login page