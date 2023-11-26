from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class Login(forms.Form):
    username = forms.CharField(max_length=17, widget=forms.TextInput(attrs={'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        else:
            raise ValidationError('your entered password or username is wrong', code='invalid_about')
