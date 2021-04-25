from  django.urls import path
import myapp.views as myapp

app_name = 'myapp'

urlpatterns = [
    path("", myapp.index, name='index'),
    path('dialog/<int:dialog_pk>/', myapp.show_dialog, name='show_dialog'),
    path('dialog/create/', myapp.dialog_create, name='dialog_create'),
    path('user/dialog/create/<int:user_id>/', myapp.user_dialog_create,
         name='user_dialog_create'),
path('user/dialog/delete/<int:pk>/', myapp.delete_dialog,
         name='delete_dialog'),

    path('dialog/member/<int:sender_pk>/message/create/',
         myapp.MessageCreate.as_view(),
         name='message_create'),
]
