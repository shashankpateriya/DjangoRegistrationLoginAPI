from rest_framework import serializers
from userlogin.models import UserRegistration

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=100, default=True)
    city = serializers.CharField(max_length=20, default=True)
    state = serializers.CharField(max_length=20, default=True)
    
    def create(self, validated_data):
        return UserRegistration.objects.create_user(**validated_data)