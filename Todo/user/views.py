from django.shortcuts import render,redirect
from .forms import CustomUserRegistrationForm
from .tokens import account_activation_generator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
# Create your views here.
def activate_email(request,user,to_email):
    mail_subject = "Activate your user account"
    message = render_to_string('user/activate_account.html',{
        "user":user.username,
        "domain":get_current_site(request).domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": account_activation_generator.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject,message,to=[to_email])
    if email.send():
        messages.success(request,f'Kindly check your inbox at {to_email} to activate your account')
    else:
        messages.error(request,f'Problem sending email to {to_email}, kindly check your email and try again')
    
def activate(request,uidb64,token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request,f'Thank you for your email confirmation. Now you can log into you account')
        return redirect('login')
    else:
        messages.error(request,f'Activation link is invalid ')
    return redirect('home')

def signup_view(request):
    if request.method=="POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active=False
            new_user.save()
            activate_email(request,new_user,form.cleaned_data.get('email'))
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()      
    return render(request,'user/signup.html',{"form":form})

# Custom User Authentication of both username and password
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
