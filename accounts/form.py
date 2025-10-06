from django import forms
from .models import My_User
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm ,UserChangeForm


class Create_UserForm(UserCreationForm):
    class Meta:
        model = My_User
        fields = ["username", "email", "phone_number", "address", "password1", "password2"]

class change_profileForm(UserChangeForm):
    class Meta:
        model = My_User
        fields = ["username", "email", "phone_number", "address"]


class LoginForm (AuthenticationForm):
     username = forms.CharField()
     password = forms.CharField()