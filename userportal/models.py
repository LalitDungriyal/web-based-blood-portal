from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class participants(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField(default='0')
    date=models.DateField(default=timezone.now)
    bloodgroup=models.CharField(max_length=4)
    
class historydonations(models.Model):
    username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField(default='0')
    date=models.DateField(default=timezone.now)
    bloodgroup=models.CharField(max_length=4)
    
class profile(models.Model):
    user=models.OneToOneField(User,null=False, blank=True, on_delete=models.CASCADE)
    image=models.ImageField(default='user.svg',null=False, blank=True,upload_to='pics')
    age=models.IntegerField(default='0')
    bloodgroup=models.CharField(max_length=4)


class event(models.Model):
    Eventname=models.CharField(max_length=100)
    eventtime=models.TimeField(default='0')
    eventdate=models.DateField(default=timezone.now)
    organizingcommunity=models.CharField(max_length=4)