from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login

from .forms import AuthUserForm, RegisterUserForm


class RegisterUserView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'authorization/reg.html'
    success_url = reverse_lazy('marketplace1:product_list')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        valid = super(RegisterUserView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
        new_user = authenticate(username=username, password=password)
        new_user = form.save()
        login(self.request, new_user)
        return valid


class AuthUserView(LoginView):
    template_name = 'authorization/auth.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('marketplace1:product_list')


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('marketplace1:product_list')