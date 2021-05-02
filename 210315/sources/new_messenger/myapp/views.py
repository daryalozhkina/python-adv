from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from myapp.forms import DialogMessageForm

from myapp.models import Dialog, DialogMemebers, Message

@login_required
def index(request):
    dialogues = request.user.dialogs.select_related('dialog').all()
    context = {
        'page_title': 'диалоги',
        'dialogues': dialogues,
    }

    return render(request, 'myapp/index.html', context)

def show_dialog(request):
    dialog = get_object_or_404(Dialog, pk=dialog_pk)
    _dialog_members = DialogMemebers.objects.filter(dialog=dialog)
    dialog_members = _dialog_members.exclude(member=request.user). \
        select_related('member')
    dialog_messages = Message.objects.filter(sender__in=_dialog_members). \
        select_related('sender__member')

    context = {
        'page_title': 'диалог',
        'dialog': dialog,
        'dialog_members': dialog_members,
        'dialog_messages': dialog_messages,
    }

    return render(request, 'myapp/show_dialog.html', context)

def dialog_create(request):
    dialogues = request.user.dialogs.select_related('dialog').all(). \
        values_list('dialog_id', flat=True)
    interlocutors = DialogMemebers.objects.filter(dialog__in=dialogues).\
        values_list('member_id', flat=True)
    new_interlocutors = User.objects.exclude(pk__in=interlocutors)

    context = {
        'page_title': 'новый диалог',
        'new_interlocutors': new_interlocutors,
    }
    return render(request, 'myapp/dialog_create.html', context)


def user_dialog_create(request, user_id):
    interlocutor = User.objects.get(pk=user_id)
    dialog = Dialog.objects.create(
        name=interlocutor.username
    )
    DialogMemebers.objects.create(
        dialog=dialog,
        member=request.user,
        role=DialogMemebers.CREATOR
    )
    DialogMemebers.objects.create(
        dialog=dialog,
        member=interlocutor,
        role=DialogMemebers.INTERLOCUTOR
    )

    return HttpResponseRedirect(
        reverse('main:dialog_show', kwargs={'dialog_pk': dialog.pk})
    )

def dialog_delete(request, pk):
    instance = get_object_or_404(Dialog, pk=pk)
    instance.delete()
    return HttpResponseRedirect(reverse('main:index'))


class DialogMessageCreate(CreateView):
    model = Message
    form_class = DialogMessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        sender_pk = self.request.resolver_match.kwargs['sender_pk']
        form.initial['sender'] = sender_pk

        return context

    def get_success_url(self):
        return reverse(
            'main:dialog_show',
            kwargs={'dialog_pk': self.object.sender.dialog_id}
        )

    def dialog_new_messages(request, dialog_pk):
        if request.is_ajax():
            dialog = Dialog.objects.filter(pk=dialog_pk).first()
            status = False
            new_messages = None
            if dialog:
                status = True
                _new_messages = dialog.get_messages_new(request.user.pk)
                # _new_messages.update(read=True)
                new_messages = [{'pk': el.pk,
                                 'username': el.sender.member.username,
                                 'created': el.created.strftime('%Y.%m.%d %H:%M'),
                                 'text': el.text}
                                for el in _new_messages]
            return JsonResponse({
                'status': status,
                'new_messages': new_messages,
})
