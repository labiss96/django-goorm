from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Profile(AbstractUser):
    #profile_img=models.CharField
    start_year=models.CharField(max_length=200, null=True)    
    sex= models.CharField(max_length=5, null=True)