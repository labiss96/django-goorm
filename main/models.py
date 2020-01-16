from django.db import models
from accounts.models import Profile
from goorm.models import *

# Create your models here.


class Buying_Log(models.Model):
    buyer = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name= 'buyer')
    product = models.ForeignKey(Tobacco, on_delete = models.CASCADE, related_name= 'product') 
    date = models.DateField()

    def __str__(self) :
        return self.buyer.username 

    def as_dict(self):
        return {'date':str(self.date)}

    