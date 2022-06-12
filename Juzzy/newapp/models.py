from django.db import models

# Create your models here.
class Schools(models.Model):
    name = models.CharField(max_lenght=23)
    address = models.CharField(max_lenght=23)

class Country(models.Model):
    name = models.CharField(max_lenght=23)    