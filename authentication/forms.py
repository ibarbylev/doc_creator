import re

from django import forms
from django.contrib.auth.models import User

from authentication.models import UserProfile

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {'password': forms.PasswordInput()}

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError('Invalid email format')

        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
