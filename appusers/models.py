from django.db import models

# Create your models here.
class Allusers(models.Model):
    fullname=models.CharField(max_length=128,null=False)
    address=models.CharField(max_length=128)
    email=models.EmailField(max_length=128,unique=True)
    password=models.CharField(max_length=128)