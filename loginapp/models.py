from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=550,null=True,blank=True)
    password=models.CharField(max_length=550,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    contactno=models.IntegerField(max_length=10,null=True,blank=True)
