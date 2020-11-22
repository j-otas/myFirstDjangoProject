from django.db import models
from django.contrib.auth import get_user_model
from marketplace1.models import Product
from django.utils import timezone
from account.models import Account

User = get_user_model()

class Auction(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()

    def __str__(self):
        return "Organizer: " + str(self.organizer or None)

    class Meta:
        verbose_name = 'Аукцион'
        verbose_name_plural = 'Аукционы'


class Bid(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(null=True)

    def __str__(self):
        return "Auction product: " + str(self.auction.product.title or None) + "; Author:" + str(self.author or None)

    class Meta:
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'

