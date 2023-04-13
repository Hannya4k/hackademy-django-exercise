from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50)
    #username = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    
    
class Profile(models.Model):
    url = models.CharField(max_length=50)
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=60)
    group = models.CharField(max_length=60)