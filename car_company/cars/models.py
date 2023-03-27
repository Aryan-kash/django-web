from django.db import models

# Create your models here.
class image(models.Model):
  
               Car_Id=models.CharField(max_length=100)
               Car_name=models.CharField(max_length=100)
               Car_type=models.CharField(max_length=100)
               Rate_perday=models.CharField(max_length=100)
               Photo=models.FileField(upload_to='media/')
               img_url=models.CharField(max_length=100)