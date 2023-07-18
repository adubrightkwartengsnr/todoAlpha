from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .authentication import EmailOrUsernameBackend
urlpatterns = [
    path("signup/",views.signup_view,name = 'signup'),
    path("login/",views.CustomLoginView.as_view(),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name='user/logout.html'),name="logout"),
    path("activate/<uidb64>/<token>/",views.activate,name="activate"),
]