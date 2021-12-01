from django.urls import path
from . import views


app_name = "admin_panel"

urlpatterns = [
    path('', views.main_admin_panel, name='admin_main'),
    path('/tables/<int:pk>/', views.admin_current_table, name='admin_current_table'),
    path('/accept_data', views.accept_change_data, name='accept_data'),
    path('/add_modal_form', views.add_modal_form, name='add_modal_form'),
    path('/accept_add_data', views.accept_add_data, name='accept_add_data'),

]
