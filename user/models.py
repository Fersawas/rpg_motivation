from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import U


class UserMain(AbstractUser):
    
    username = models.CharField()