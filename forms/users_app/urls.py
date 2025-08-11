from django.contrib import admin
from django.urls import path,include
from .views import register,profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/",register,name="register"),
    path("accounts/login/", auth_views.LoginView.as_view(),name="login"),
    path("profile/",profile,name="profile")
]