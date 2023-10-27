from django.db import models

# Create your models here.
class Creators(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)