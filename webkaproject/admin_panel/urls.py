from django.urls import path
from . import views


app_name = "admin_panel"

urlpatterns = [
    path('', views.main_admin_panel, name='admin_main'),
    path('/tables/<int:pk>/', views.admin_current_table, name='admin_current_table'),
    path('/tables/<int:pk>/<int:idd>/', views.edit_table, name='edit_table'),
    path('/accept_data', views.accept_change_data, name='accept_data'),

]
