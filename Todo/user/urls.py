from django.urls import path
from . import views
from django.contrib.auth import views as authviews
urlpatterns = [
    path("signup/",views.signup_view,name = 'signup'),
    path("login/",views.CustomLoginView.as_view(template_name='user/login.html'),name="login"),
    path("activate/<uidb64>/<token>/",views.activate,name='activate'),
]