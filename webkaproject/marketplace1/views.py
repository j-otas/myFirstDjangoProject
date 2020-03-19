from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView
from django.urls import reverse_lazy

def product_list(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'marketplace/content.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'marketplace/product_detail.html', {'product': product})


class NewProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'marketplace/product_new.html'
    success_url = reverse_lazy('marketplace1:product_list')

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
