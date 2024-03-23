from django.db import models

# Create your models here.
class Empmodel(models.Model):
    name=models.CharField(max_length=64)
    year=models.IntegerField()
    branch=models.CharField(max_length=10)
    domain=models.CharField(max_length=64)
    mode=models.CharField(max_length=64)
