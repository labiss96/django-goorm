from django.db import models
from django.contrib.auth.models import AbstractUser
from django_fields import DefaultStaticImageField

# Create your models here.

class Profile(AbstractUser):
    start_year=models.CharField(max_length=200, null=True)    
    sex= models.CharField(max_length=5, null=True)
    profile_img = DefaultStaticImageField(upload_to='profile_img/', blank=True, default_image_path='images/default_profile_img.png')