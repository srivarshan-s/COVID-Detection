from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=25)
    location = models.CharField(max_length=50)
    xcoord = models.FloatField()
    ycoord = models.FloatField()
    fee = models.IntegerField()

    def __str__(self):
        return self.username


class UserImage(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="covid/static/covid/userImage/")

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=50)
    xcoord = models.FloatField()
    ycoord = models.FloatField()
    fee = models.IntegerField()

    def __str__(self):
        return self.name