from django.db import models

class form(models.Model):
    name=models.CharField(max_length=40)
    description= models.CharField(max_length=200)
    image=models.ImageField()



# Create your models here.
