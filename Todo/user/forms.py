from typing import Any
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth import login

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = CustomUser
        fields = ["username","email","password1","password2"]
        
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)
        # Remove the username field
        self.fields.pop('username')
        # Add the username or email field
        self.fields['username_or_email'] = UsernameField(widget=forms.TextInput(attrs={'autofocus':True}))
    
    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')
        if username_or_email and password:
            user_model = get_user_model()
            try:
                user = user_model.objects.get(Q(username = username_or_email)|Q(email=username_or_email))
                
            except user_model.DoesNotExist:
                user = None
            if user is None or not user.check_password(password):
                raise forms.ValidationError('Invalid username/email or password')
            login(self.request,user)
        return self.cleaned_data        
    
   