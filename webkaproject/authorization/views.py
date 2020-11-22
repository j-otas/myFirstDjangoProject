from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from .forms import AuthUserForm
from webkaproject import settings
from account.forms import RegistrationForm



class AuthUserView(LoginView):
    template_name = 'authorization/auth.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('marketplace1:product_list')


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('marketplace1:product_list')
