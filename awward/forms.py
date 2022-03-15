from .models import Project, Rate, User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']