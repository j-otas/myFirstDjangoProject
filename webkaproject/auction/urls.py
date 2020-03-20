from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from auction.views import AuctionListView
urlpatterns = [
    path('', AuctionListView.as_view())
]

