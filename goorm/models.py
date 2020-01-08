from django.db import models
class Tobacco(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    price = models.IntegerField(blank=True)
    rel_date = models.DateTimeField(blank=True)
    nicotine =  models.FloatField()
    TAR = models.FloatField()
    feel_of_hit = models.CharField(max_length=10)
    score = models.FloatField(default=0)
    #total_like = models.PositiveIntegerField(default=0)
    #like_user = models.ManyToManyField()
    isMenthol = models.BooleanField(default = False)
    img = models.ImageField(blank=True, null=True)
    


    def __str__(self):
        return self.name

# Create your models here.
