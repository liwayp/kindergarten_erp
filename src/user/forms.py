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

class AddEmployeeForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full mt-1 p-2 border border-gray-300 rounded-lg'
        }),
        label='Пароль'
    )

    class Meta:
        model = Users
        fields = ['email', 'name', 'role', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'w-full mt-1 p-2 border border-gray-300 rounded-lg'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full mt-1 p-2 border border-gray-300 rounded-lg'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full mt-1 p-2 border border-gray-300 rounded-lg'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = [
            (key, value) for key, value in self.fields['role'].choices
            if key not in ('admin', 'parents')
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email
