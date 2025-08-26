# core/context_processors.py
from conversation.models import ConversationMessage


def unread_message_count(request):
    if request.user.is_authenticated:
        count = ConversationMessage.objects.filter(
            conversation__members=request.user,  # belongs to a conversation I’m in
            is_read=False                        # not read yet
        ).exclude(
            created_by=request.user              # don’t count my own messages
        ).count()
        return {'unread_message_count': count}
    return {}