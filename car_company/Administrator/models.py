from django.db import models

# Create your models here.




class admin_user(models.Model):


    username =models.CharField(max_length=100)
    password =models.CharField(max_length=60)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
