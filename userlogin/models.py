from django.db import models
from django.db.models.expressions import F

# Create your models here.
class UserRegistration(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default=False, unique=True)

    def __str__(self) -> str:
        return self.name