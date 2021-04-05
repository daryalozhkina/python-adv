from  django.urls import path
import myapp.views as myapp

app_name = 'myapp'

urlpatterns = [
    path("", myapp.index),
]
