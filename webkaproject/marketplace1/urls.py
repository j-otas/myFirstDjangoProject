from django.urls import path
from . import views


app_name = "marketplace1"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.NewProductView.as_view(), name='product_new'),
    path('product/<int:pk>/edit', views.product_edit, name='product_edit'),
    path('personal', views.Personal.as_view(), name='personal_page'),
    path('refill', views.BalanceRefill.as_view(), name='refill_page'),

]
