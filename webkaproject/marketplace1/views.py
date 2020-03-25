from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Product, UserDetails
from .forms import ProductForm
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView, View, TemplateView
from django.urls import reverse_lazy
from decimal import *

def product_list(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'marketplace/content.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'marketplace/product_detail.html', {'product': product})


def product_new(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('marketplace1:product_detail', pk= product.pk)
    else:
        form = ProductForm()
        return render(request, 'marketplace/product_new.html', {'form': form})


class Personal (View):
    def get(self, request, *args, **kwargs):
        cur_user = self.request.user
        if cur_user.is_authenticated:
            return render(self.request, 'personal/personal_main.html', {'cur_user': cur_user})


class BalanceRefill (TemplateView):
    template_name = 'marketplace/refill.html'

    def post(self, request, *args, **kwargs):
        cur_user = UserDetails.objects.get(user = request.user)
        money = Decimal(request.POST['count_money'])
        cur_user.balance += money

        cur_user.save()
        return render(request, 'marketplace/refill.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('marketplace1:product_detail', pk=product.pk)

    else:
        form = ProductForm(instance=product)
    return render(request, 'marketplace/product_edit.html', {'form': form})
