from django.urls import path
from userlogin import views

urlpatterns = [
    # path('register', views.register, name="register"),
    # path('login', views.login, name="login"),
    path('usermodel', views.UserRegister.as_view(), name="usermodel"),
    path('usermodellogin', views.UserLogin.as_view(), name="usermodellogin"),
    path('userlogintoken', views.UserLoginToken.as_view(), name="userlogintoken")
]
