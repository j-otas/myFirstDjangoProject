from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
import os

class MyAccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, username, country, cellphone,  password = None):
        if not email or not email or not cellphone:
            raise ValueError("Не указаны необходимые данные пользователья")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            country = country,
            cellphone = cellphone
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, cellphone, password):
        if not email or not email or not cellphone:
            raise ValueError("Не указаны необходимые данные пользователья")

        user = self.create_user(
            email = self.normalize_email(email),
            username = "Admin",
            first_name = "Konstantin",
            last_name="Grunes",
            country="Irkutsk",
            cellphone=cellphone,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

class Account(AbstractBaseUser):

    email = models.EmailField(verbose_name = "email", max_length = 60, unique = True, default = "")
    username = models.CharField(max_length = 30, unique = True)

    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    cellphone = PhoneNumberField(null=True, blank=True, unique=True)
    country = models.CharField(max_length = 35)
    avatar = models.ImageField(blank=True, null=True, verbose_name="Аватар пользователя", upload_to='user_images',
                              default="no_image.png")

    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = 'last login', auto_now = True)

    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_moderated = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["cellphone"]

    objects = MyAccountManager()

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_name + ', ' + self.last_name + ', ' + self.cellphone.as_e164

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(models.signals.post_delete, sender=Account)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Удаление изображений из файловой системы
    """
    if instance.image:
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)


@receiver(models.signals.pre_save, sender=Account)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Удаление старых изображений из файловой системы при обновлении
    """
    if not instance.pk:
        return False

    try:
        old_file = Account.objects.get(pk=instance.pk).avatar
        if not old_file:
            return False
    except Account.DoesNotExist:
        return False

    new_file = instance.avatar
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


