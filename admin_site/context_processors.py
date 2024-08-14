from contact.models import Message

def get_message_unread(request):
    unread_count = Message.unread_count()
    unread_messages = Message.objects.filter(is_read=False)
    return {'messages_count': unread_count,'unread_messages':unread_messages}

# unread_messages = ContactMessage.objects.filter(is_read=False)