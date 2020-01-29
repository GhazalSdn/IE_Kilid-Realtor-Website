from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# Create your models here.
class dataUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=5)
    phoneNum = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    userLevel = models.BooleanField(default=False)


class kilidUser(AbstractUser):
    phoneNum = models.CharField(max_length=50)
    isManager = models.BooleanField(default=False)

class Housing(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    type = models.CharField(max_length=50)
    area = models.IntegerField()
    bedrooms = models.IntegerField()
    parkings = models.IntegerField()
    locality = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    pic =  models.CharField(max_length=50)
    estate = models.CharField(max_length=50)
    star = models.BooleanField()
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    houseID = models.CharField(max_length=50)
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    time = models.DateTimeField()
