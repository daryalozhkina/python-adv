from django.contrib import admin

from myapp.models import Dialog, Message, DialogMemebers

admin.site.register(Dialog)
admin.site.register(DialogMemebers)
admin.site.register(Message)



