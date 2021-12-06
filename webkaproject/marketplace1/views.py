from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Product, Category, FavoriteProduct
from account.models import Account
from .forms import ProductForm
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView, View, TemplateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from decimal import *
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.templatetags.static import static
from django.http import JsonResponse
from django.template.loader import render_to_string
from account.forms import RegistrationForm
from django.contrib.auth import authenticate, login

categories = Category.objects.all()

def product_list(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'marketplace/content.html', {'products': products , 'categories':categories})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    is_fav = False
    try:
        fav = FavoriteProduct.objects.get(user=request.user, product=product)
    except FavoriteProduct.DoesNotExist:
        fav = False
    if fav:
        is_fav = True
    return render(request, 'marketplace/product_detail.html', {'product': product,'categories': categories, 'is_fav':is_fav})


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

class Personal (View):
    def get(self, request, *args, **kwargs):
        account_pk = self.kwargs['pk']
        user = self.request.user
        if user.is_authenticated:
            cur_user = user
        cur_user = Account.objects.get(pk=account_pk)
        # if cur_user:
        users_products = Product.objects.filter(author=cur_user)
        return render(self.request, 'personal/personal_main.html', {'cur_user': cur_user, 'users_products': users_products, 'categories': categories})

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
    return render(request, 'marketplace/product_edit.html', {'form': form, 'product_pk':product.pk,'categories': categories})

class SearchResultsView(ListView):
    model = Product
    template_name = 'marketplace/product_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        #print(query+"fdfdfdfefef")
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        return context

def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return HttpResponseRedirect(reverse_lazy("marketplace1:product_list"))
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

class FavoriteProductsList(ListView):
    model = FavoriteProduct
    template_name = 'marketplace/favorite_products_list.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        data = {'favorites': FavoriteProduct.objects.filter(user=self.request.user)}
        temp = FavoriteProduct.objects.filter(user=self.request.user)
        return data

def add_favorite_product(request,pk):

    if request.is_ajax():
        product = Product.objects.get(pk=pk)
        favorite = FavoriteProduct(user=request.user, product=product)
        favorite.save()
        context = {}
        context['is_fav'] = True
        context['product'] = product
        result = render_to_string('includes/favorite_block.html', context)
        return JsonResponse({'result': result})

def delete_favorite_product(request,pk):

    if request.is_ajax():
        try:
            product = Product.objects.get(pk=pk)
            favorite = FavoriteProduct.objects.get(user=request.user, product=product)
            favorite.delete()
            context = {}
            context['is_fav'] = False
            context['product'] = product
            result = render_to_string('includes/favorite_block.html', context)
            return JsonResponse({'result': result})
        except Product.DoesNotExist:
            return HttpResponseNotFound("<h2>Favorite not found</h2>")

def delete_from_favorit_list(request,pk):
    if request.is_ajax():
        try:
            print("sdadsad")
            product = Product.objects.get(pk=pk)
            favorite = FavoriteProduct.objects.get(user=request.user, product=product)
            favorite.delete()
            return JsonResponse({'result': 'success'})
        except Product.DoesNotExist:
            return HttpResponseNotFound("<h2>Favorite not found</h2>")

def personal_edit(request,pk):
    cur_user = Account.objects.get(pk=pk)
    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=cur_user)
        if form.is_valid():

            cur_user = form.save(commit=False)
            cur_user.save()
            login(request,cur_user)
            return redirect('marketplace1:personal_page', pk=cur_user.pk)


    else:
        form = RegistrationForm(instance=cur_user)
    return render(request, 'personal/personal_edit.html',
                  {'form': form,})

