from django.db import models

# Create your models here.
class Products (models.Model):
    name = models.CharField(max_length=60)
    provider = models.CharField(max_length=200)
    existences = models.PositiveIntegerField()
    date = models.DateField()
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=60)
