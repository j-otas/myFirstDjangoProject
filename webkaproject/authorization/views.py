from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

from .forms import AuthUserForm, RegisterUserForm


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'authorization/reg.html'
    success_url = reverse_lazy('marketplace1:product_list')
    success_msg = 'Пользователь успешно создан'


class AuthUserView(LoginView):
    template_name = 'authorization/auth.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('marketplace1:product_list')