from django.urls import path
from . import views

app_name = 'authorization'

urlpatterns = [
    path('reg/', views.RegisterUserView, name='reg_page'),
    path('', views.AuthUserView.as_view(), name='auth_page'),
    path('logout', views.LogoutView.as_view(), name='logout'),

]
