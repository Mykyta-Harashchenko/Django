from django.forms import CharField, ImageField, TextInput, FileInput, EmailInput, EmailField, PasswordInput, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    email = CharField(max_length=30, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    password1 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileForm(ModelForm):
    avatar = ImageField(widget=FileInput())

    class Meta:
        model = Profile
        fields = ['avatar']