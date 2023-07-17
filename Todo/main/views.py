from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="user/login")
def home(request):
    return render(request,'main/home.html')
