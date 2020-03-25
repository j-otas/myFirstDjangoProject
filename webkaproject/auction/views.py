from django.shortcuts import render
from .models import Auction
from marketplace1.models import UserDetails
from django.views.generic import TemplateView, ListView, DetailView
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class AuctionListView(ListView):
    model = Auction
    template_name = 'auction/auction_list.html'
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['publisher'] = self.publisher
    #     return context


class AuctionDetailView(ListView):
    model = Auction
    template_name = 'auction/auction_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # get the default context data
        user = get_object_or_404(User, id=self.request.user.id)
        userDetails = get_object_or_404(UserDetails, user_id=user.id)
        context['selected_auction'] = Auction.objects.get(pk= self.kwargs['pk'])  # add extra field to the context
        context['balance'] = userDetails.balance
        return context
