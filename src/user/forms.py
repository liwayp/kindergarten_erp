from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Users

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Users
        fields = ['name', 'email', 'role', 'password']


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))

