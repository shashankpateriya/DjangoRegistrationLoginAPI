from django.contrib import admin
from django.urls import path
from userlogin import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('usermodel', views.user_model_register, name="usermodel"),
    path('usermodellogin', views.user_model_login, name="usermodellogin")
]
