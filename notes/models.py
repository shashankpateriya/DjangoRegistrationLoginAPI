from django.db import models
from userlogin.models import UserRegistration

class Notes(models.Model):
    user_id = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)