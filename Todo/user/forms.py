from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth import login,authenticate
from django.contrib import messages


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = CustomUser
        fields = ["username","email","password1","password2"]
    
class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)