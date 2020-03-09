from django.shortcuts import render


def product_list(request):
    return render(request, 'marketplace/product_list.html', {})
