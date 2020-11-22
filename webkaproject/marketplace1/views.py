from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Product, Category
from account.models import Account
from .forms import ProductForm
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView, View, TemplateView, ListView
from django.urls import reverse_lazy
from django.db.models import Q
from decimal import *
from django.http import HttpResponse,HttpResponseRedirect


categories = Category.objects.all()

def product_list(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'marketplace/content.html', {'products': products , 'categories':categories})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'marketplace/product_detail.html', {'product': product,'categories': categories})


class NewProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'marketplace/product_new.html'
    success_url = reverse_lazy('marketplace1:product_list')


    # def post(self, request, *args, **kwargs):
    #     form =  ProductForm(request.POST)
    #
    #     if form.is_valid():
    #         image = form.cleaned_data['image']
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    # <view logic>
    def form_valid(self, form):

        new_product = form.save(commit=False)
        new_product.author = self.request.user
        new_product.published_date = timezone.now()
        new_product.save()
        return super().form_valid(form)

# def product_new(request):
#     if request.POST:
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.author = request.user
#             product.published_date = timezone.now()
#             product.save()
#             return redirect('marketplace1:product_detail', pk= product.pk)
#     else:
#         form = ProductForm()
#         return render(request, 'marketplace/product_new.html', {'form': form})


class Personal (View):
    def get(self, request, *args, **kwargs):
        account_pk = self.kwargs['pk']
        user = self.request.user
        if user.is_authenticated:
            cur_user = user
        cur_user = Account.objects.get(pk=account_pk)
        # if cur_user:
        users_products = Product.objects.filter(author=cur_user)
        return render(self.request, 'personal/personal_main.html', {'cur_user': cur_user, 'users_products': users_products})

class BalanceRefill (TemplateView):
    template_name = 'marketplace/refill.html'

    def post(self, request, *args, **kwargs):
        cur_user = Account.objects.get(user = request.user)
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


class SearchResultsView(ListView):
    model = Product
    template_name = 'marketplace/product_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        if category == '-1' :
            product_list = Product.objects.filter(
            Q(title__icontains=query))
        elif query == None:
            product_list = Product.objects.filter(
                Q(category_id=category))
        else:
            product_list = Product.objects.filter(
                Q(title__icontains=query) & Q(category_id=category))

        return product_list
