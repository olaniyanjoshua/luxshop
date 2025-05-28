from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
   class Meta:
      model = ConversationMessage
      fields = ('content',)
      widgets = {
         'contents':forms.Textarea(attrs={
            'class':'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-blue-500'
         })
      }