from django.contrib.auth.models import User
from userlogin.models import UserRegistration
# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import json

def register(request):
    """
    Getting user details from  post request and registering that user
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        UserRegistration.objects.create(name=name, username=username, password=password, email=email)
        print(request.POST, "success")
        form_dict = {"data" : {
            "name" : name,
            "username" : username,
            "password" : password,
            "email" : email },
            "message" : "Registered"
        }
    return JsonResponse(form_dict)

def login(request):
    """
    Checking the user credentials in database for login.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        try:
            if UserRegistration.objects.filter(username=username, password=password).exists():
                success_message = {"message" : "Login successful"}
                return JsonResponse(success_message)
            else:
                wrong_message = {"message" : "Wrong credentials"}
                return JsonResponse(wrong_message)
        except Exception:
            raise ValueError

