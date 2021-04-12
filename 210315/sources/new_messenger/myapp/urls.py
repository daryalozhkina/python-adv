from  django.urls import path
import myapp.views as myapp

app_name = 'myapp'

urlpatterns = [
    path("", myapp.index, name='index'),
path('dialog/<int:dialog_pk>/', myapp.show_dialog, name='show_dialog'),
]
