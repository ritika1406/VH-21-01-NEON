from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class tweet(models.Model):
    fname = models.CharField(max_length=280,default='')
    address = models.TextField(max_length=280,default='')
    phone = models.CharField(max_length=280,default='') 
    meal = models.ForeignKey(User,on_delete=models.CASCADE) 
    datetime = models.DateTimeField(default=timezone.now)
     

    