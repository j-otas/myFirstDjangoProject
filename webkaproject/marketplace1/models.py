from django.conf import settings
from django.db import models
from django.utils import timezone
<<<<<<< HEAD
=======
from django.dispatch import receiver
import os


class UserDetails(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    cellphone = models.CharField(max_length=11, null=True, blank= True)
    country = models.CharField(max_length=45, null=True, blank= True)

>>>>>>> f881494... Added default auction page, refill balance page, personal page, user details


    class Meta:
        verbose_name = 'Подробности пользователя'
        verbose_name_plural = 'Подробности пользователя'

class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт(товар)'
        verbose_name_plural = 'Продукты(товары)'
