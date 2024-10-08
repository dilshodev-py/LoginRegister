
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import HomeTemplateView, RegisterFormView, LoginFormView, CustomLogoutView

urlpatterns = [
    path('', HomeTemplateView.as_view() , name="home"),
    path('register', RegisterFormView.as_view() , name="register"),
    path('login', LoginFormView.as_view() , name="login"),
    path('logout', CustomLogoutView.as_view() , name='logout'),
]
