let $dialogMessages;
function messageRender(message) {
    let message = $('.message-' + message.pk);
    let textMessage;
    if (!message.length) {
        let messageNew = document.createElement('li');
        messageNew.classList.add('message-' + message.pk);
        textMessage = message.username + " (" + message.created + ") - " + message.text;
        messageNew.innerHTML = textMessage;
        let parent = $dialogMessages.find('.messages-list');
        parent.prepend(messageNew);
    }
}

window.onload = function () {
    console.log('ready');

    $dialogMessages = $('.dialog-messages');
    $dialogMessages.on('click', 'a.dialog-update', function (e) {
        e.preventDefault();

    setInterval(function(){
    $('.dialog-update').trigger('click');
    }, 5);