from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import ProductForm
from django.shortcuts import redirect
from django.utils import timezone


def product_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'marketplace/product_list.html', {'posts': posts})


def product_detail(request, pk):
    product = get_object_or_404(Post, pk=pk)
    return render(request, 'marketplace/product_detail.html', {'post': product})


def product_new(request):
    if(request.POST):
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('product_detail',pk = post.pk )
    else:
        form = ProductForm()
        return render(request, 'marketplace/product_new.html', {'form': form})

def product_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('product_detail', pk=post.pk)

    else:
        form = ProductForm(instance=post)
    return render(request, 'marketplace/product_edit.html', {'form': form})
