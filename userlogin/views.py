from django.contrib.auth import authenticate
from django.http import JsonResponse, request
from django.http.response import HttpResponse
from rest_framework import serializers
from userlogin.models import UserRegistration
from rest_framework.views import APIView
from userlogin.serializers import UserSerializer
from django.db import IntegrityError
import jwt, datetime
from jwt import decode

class UserRegister(APIView):
    """
    register a user by serializing data with rest framework
    return: details of user
    """
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                success_message = {"message" : "User successfully registered",
                "data" : serializer.data}
                return JsonResponse(success_message)
            else:
                return JsonResponse(serializer.errors)
        except IntegrityError as e:
            return JsonResponse(e.__cause__)
        except TypeError:
            return JsonResponse("The user already exists")


class UserLogin(APIView):
    """
    authenticate username and password of user
    """
    def post(self, request):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        try:
            if user is not None:
                success_message = {"message" : "Login successful"}
                return JsonResponse(success_message)
            else:
                wrong_message = {"message" : "Wrong credentials"}
                return JsonResponse(wrong_message)
        except IntegrityError as e:
            return JsonResponse(e.__cause__)

class UserLoginToken(APIView):
    def post(self, request):
        try:
            user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
            if user is not None:
                payload = {
                    "user_id" : user.pk
                }
                token = jwt.encode(payload, 'secret', algorithm="HS256")
                return JsonResponse({
                    'jwt': token
                })
            else:
                return JsonResponse("Wrong credentials")
        except IntegrityError as e:
            return JsonResponse(e.__cause__)