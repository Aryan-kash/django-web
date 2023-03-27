from django.db import models

# Create your models here.



class customers(models.Model):
   
    username =models.CharField(max_length=100,primary_key=True)
    password =models.CharField(max_length=60)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    age= models.IntegerField()
    gender= models.CharField(max_length=100)
    
