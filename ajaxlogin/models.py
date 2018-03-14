from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class Login(models.Model):
#     username=models.CharField(max_length=550,null=True,blank=True)
#     password=models.CharField(max_length=550,null=True,blank=True)
#     email=models.EmailField(max_length=20,unique=True)
#     contactno=models.IntegerField(null=True,blank=True)


class Logins(models.Model):
    username=models.CharField(max_length=550,null=True,blank=True)
    password=models.CharField(max_length=550,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    contactno=models.IntegerField(null=True,blank=True)