from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# class User1(AbstractUser):
#       first_name = models.CharField(max_length=50)
#       last_name = models.CharField(max_length=60)
      
class User(AbstractUser):
   # first_name = models.CharField(max_length=50)
   # last_name = models.CharField(max_length=60)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=50)
    repeat_password = models.CharField(max_length=60)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture = models.ImageField()
    description = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)

    def __str__(self):
       return f'{self.user.username} Profile'
