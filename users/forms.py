from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Default is required=True

    """
    THis class Meta provides us with a nested namespace and keeps all
    the configuration in one place
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
