from django.shortcuts import render,redirect
from .forms import CustomUserRegistrationForm

# Create your views here.
def signup_view(request):
    if request.method=="POST":
        form = CustomUserRegistrationForm()
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active=False
            new_user.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()      
    return render(request,'user/signup.html',{"form":form})

def login_view(request):
    return render(request,'user.login.html')