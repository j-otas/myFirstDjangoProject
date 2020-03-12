from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Comment
from django.utils import timezone


def product_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'marketplace/product_list.html', {'posts': posts})


def product_detail(request, pk):
    product = get_object_or_404(Post, pk=pk)
    return render(request, 'marketplace/product_detail.html', {'post': product})