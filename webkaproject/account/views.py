from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")

            new_account = form.save(commit=False)
            new_account.set_password(raw_password)
            new_account.save()

            login(request, new_account)
            return render(request, 'marketplace/content.html', {'auth_user': new_account})
        else:
            context["reg_form"] = form
    else: #GET request
        form = RegistrationForm()
        context['reg_form'] = form
    return render(request, 'authorization/reg.html', context)
