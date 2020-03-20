from django.conf import settings

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
import os


class UserDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    cellphone = models.CharField(max_length=11)
    country = models.CharField(max_length=45)

    def __str__(self):
        user = User.objects.get(id=self.user_id)
        return "id=" + str(self.pk) + " username=" + user.username + " email=" + user.email

class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    published_date = models.DateTimeField(blank=True, null=True)
    cost = models.fields.IntegerField(blank=False, null=True, verbose_name="Цена")
    image = models.ImageField(blank=True, null=True, verbose_name="Изображение", upload_to='product_images/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # def delete(self, *args, **kwargs):
    #     self.image.delete()
    #     super(Product, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт(товар)'
        verbose_name_plural = 'Продукты(товары)'


@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Удаление изображений из файловой системы
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Удаление старых изображений из файловой системы при обновлении
    """
    if not instance.pk:
        return False

    try:
        old_file = Product.objects.get(pk=instance.pk).image
    except Product.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
