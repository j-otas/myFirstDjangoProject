from django.conf import settings


from django.db import models
from django.utils import timezone
from django.dispatch import receiver
import os
from webkaproject.settings import STATIC_URL,STATIC_ROOT
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, related_name = "products", on_delete = models.CASCADE)

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    published_date = models.DateTimeField(blank=True, null=True)
    cost = models.fields.IntegerField(blank=False, null=True, verbose_name="Цена")
    image = models.ImageField(blank=True, null=True, verbose_name="Изображение", upload_to='product_images/', default="no_image.png")
    is_active = models.BooleanField(default = False)



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
        if not old_file:
            return False
    except Product.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
