from django import forms
from django.contrib.auth.models import User

from authentication.models import UserProfile


class UserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
