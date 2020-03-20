from django.db import models
from django.contrib.auth.models import User
from marketplace1.models import Product


class Auction(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()

    def __str__(self):
        return "Organizer: "+ str(self.organizer)

    class Meta:
        verbose_name = 'Аукцион'
        verbose_name_plural = 'Аукционы'