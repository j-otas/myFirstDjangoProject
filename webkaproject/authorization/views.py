from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from marketplace1.models import UserDetails
from .forms import AuthUserForm, RegisterUserForm
from authorization.forms import UserDetailForm
from webkaproject import settings

def RegisterUserView(request):
    if request.method =='POST':
        reg_form = RegisterUserForm(request.POST)
        detail_user_form = UserDetailForm(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            username, password = reg_form.cleaned_data.get('username'), reg_form.cleaned_data.get('password')
            new_user.set_password(password)
            new_user.save()

            detail_for_new_user = detail_user_form.save(commit=False)
            detail_for_new_user.user = new_user
            detail_for_new_user.save()
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)

            return render(request, 'marketplace/content.html', {'auth_user': auth_user} )
    else:
        reg_form = RegisterUserForm()
        detail_user_form = UserDetailForm()
    return render(request, 'authorization/reg.html', {'reg_form': reg_form, 'detail_user_form': detail_user_form})


class AuthUserView(LoginView):
    template_name = 'authorization/auth.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('marketplace1:product_list')


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('marketplace1:product_list')