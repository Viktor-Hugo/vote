from django.db import models
from django.conf import settings

# Create your models here.
class Order(models.Model):
    teams = models.ManyToManyField(
            settings.AUTH_USER_MODEL, 
            related_name='orders',
            through='Bid'    
        )
    price = models.IntegerField(default=0)

class Bid(models.Model):
    team = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.IntegerField(default=0)