from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    userProfile=models.ImageField(upload_to="userProfile")