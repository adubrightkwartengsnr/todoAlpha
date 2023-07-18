from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .authentication import EmailOrUsernameBackend
urlpatterns = [
    path("signup/",views.signup_view,name = 'signup'),
    path("login/",views.CustomLoginView.as_view(),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name='user/logout.html'),name="logout"),
    path("activate/<uidb64>/<token>/",views.activate,name="activate"),
    path("password-reset",auth_views.PasswordResetView.as_view(template_name='user/password-reset.html'),name='password_reset'),
    path("password-reset-done",auth_views.PasswordResetDoneView.as_view(template_name="user/password-reset-done.html"),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='user/password-reset-confirm.html'), name='password_reset_confirm'),
    path("password-complete",auth_views.PasswordResetCompleteView.as_view(template_name='user/password-reset-complete.html'),name="password_reset_complete")
]