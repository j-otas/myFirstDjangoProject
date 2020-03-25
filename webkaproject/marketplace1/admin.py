from django.contrib import admin
from .models import Product
from .models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'balance', 'cellphone', 'photo']

admin.site.register(Product)
admin.site.register(UserDetails, UserDetailsAdmin )
