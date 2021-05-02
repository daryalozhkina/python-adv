from  django.urls import path

import myapp.views as myapp

app_name = 'myapp'

urlpatterns = [
    path('', myapp.index, name='index'),

    path('dialog/show/<int:dialog_pk>/', myapp.show_dialog, name='show_dialog'),

    path('dialog/create/', myapp.dialog_create, name='dialog_create'),

    path('user/dialog/create/<int:user_id>/', myapp.user_dialog_create,
         name='user_dialog_create'),

    path('user/dialog/delete/<int:pk>/', myapp.dialog_delete,
         name='dialog_delete'),

    path('dialog/member/<int:sender_pk>/message/create/',
         myapp.DialogMessageCreate.as_view(),
         name='dialog_message_create'),

    path('user/dialog/new/messages/<int:dialog_pk>/',
         myapp.dialog_new_messages,
         name='dialog_new_messages'),
]
