from django.urls import path
from . import views


app_name = "messenger"

urlpatterns = [
    path('', views.Dialog_list.as_view(), name='dialog_list'),
    path('<chat_id>/', views.MessagesView.as_view(), name='messages'),
    path('create/<friend_id>/', views.create_dialog, name='create_dialog'),
    path('delete/<chat_id>/', views.delete_dialog, name='delete_chat'),

    path('get_messages/<chat_id>/', views.get_messages, name='get_messages'),
    path('get/new_mes_count/', views.get_new_mes_count, name='get_new_mes_count'),
    path('get/update_dialogs/', views.update_chats_list, name='update_dialogs'),
]
