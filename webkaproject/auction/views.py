from django.shortcuts import render
from .models import Auction
from django.views.generic import TemplateView, ListView


class AuctionListView(ListView):
    model = Auction
    template_name = 'auction/auction_list.html'
