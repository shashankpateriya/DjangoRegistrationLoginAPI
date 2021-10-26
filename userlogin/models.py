from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRegistration(User):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, default=True)
    city = models.TextField(max_length=20, default=True)
    state = models.TextField(max_length=20, default=True)