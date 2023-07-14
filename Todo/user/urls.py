from django.urls import path
from . import views
urlpatterns = [
    path("signup/",views.signup_view,name = 'signup'),
    path("login/",views.login_view,name="login"),
    path("activate/<uidb64>/<token>/",views.activate,name='activate')
]