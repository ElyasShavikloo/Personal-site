from django import forms
from django.core.exceptions import ValidationError
from blog.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع چیست؟',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "چه چیزی می خواهید بگویید؟"
            })
        }






