from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


FORM_ATTRS = {
    'class': 'form-control'
}


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=128, label='Username', widget=forms.TextInput(attrs=FORM_ATTRS))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=FORM_ATTRS))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs=FORM_ATTRS))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=FORM_ATTRS))
    avatar = forms.ImageField(label='Avatar', widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'avatar')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=128, label='Username', widget=forms.TextInput(attrs=FORM_ATTRS))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=FORM_ATTRS))
