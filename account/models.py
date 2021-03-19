from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #is_student = models.BooleanField(default=False)
    #is_faculty = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Donor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    


class Ngo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)