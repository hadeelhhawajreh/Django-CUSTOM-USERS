from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class meta:
        model=CustomUser
        fields = ('username', 'email')
class CustomUserChangeForm(UserChangeForm):
    class meta:
        model=CustomUser
        fields = ('username', 'email')