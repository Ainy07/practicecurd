from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email =models.EmailField(max_length=250)
    password =models.CharField(max_length=550)
    company =models.CharField(max_length=200)
    areacode =models.IntegerField()
    contact =models.IntegerField()
    subject =models.CharField(max_length=200)
    