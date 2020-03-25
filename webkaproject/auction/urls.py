from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from auction.views import AuctionListView, AuctionDetailView

app_name = 'auction'

urlpatterns = [
    path('', AuctionListView.as_view(), name = 'auction_main'),
    path('lot/<int:pk>', AuctionDetailView.as_view(), name = 'auction_detail')
]

