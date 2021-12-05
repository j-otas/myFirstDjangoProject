from django.urls import path
from . import views


app_name = "marketplace1"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product/new/', views.NewProductView.as_view(), name='product_new'),
    path('product/<int:pk>/edit', views.product_edit, name='product_edit'),
    path('personal/<int:pk>', views.Personal.as_view(), name='personal_page'),
    path('refill', views.BalanceRefill.as_view(), name='refill_page'),
    path('search', views.SearchResultsView.as_view(), name='search_results'),
    path('favorite', views.FavoriteProductsList.as_view(), name='favorite_products'),
    path('product/<int:pk>/favorite_add', views.add_favorite_product, name='add_favorite_product'),
    path('product/<int:pk>/favorite_delete', views.delete_favorite_product, name='delete_favorite_product'),
    path('product/<int:pk>/favorite_list_delete', views.delete_from_favorit_list, name='delete_from_favorit_list'),

]
