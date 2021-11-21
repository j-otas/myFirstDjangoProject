from django.urls import path
from . import views


app_name = "admin_panel"

urlpatterns = [
    path('', views.main_admin_panel, name='admin_main'),

]
