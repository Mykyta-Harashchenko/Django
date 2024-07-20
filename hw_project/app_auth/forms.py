from django.forms import CharField, ImageField, TextInput, FileInput, EmailInput, EmailField, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(max_length=30, required=True, widget=EmailInput(attrs={'class': 'form-control'}))
    password_1 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))
    password_2 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))
    class Meta:

        model = User
        fields = ['username', 'email', 'password_1', 'password_2']


class LoginForm(AuthenticationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']