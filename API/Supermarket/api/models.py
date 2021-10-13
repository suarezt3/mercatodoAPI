from django.db import models

# Create your models here.
class Products (models.Model):
    name = models.CharField(max_length=60)
    provider = models.CharField(max_length=200)
    existences = models.PositiveIntegerField()
    date = models.DateField()
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=60)


class Supplier (models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    telephone = models.PositiveIntegerField()
    total_products = models.PositiveIntegerField()

employee_position = [(1, 'Empleado'), (2, 'Administrador')]

class Employee (models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telephone = models.PositiveIntegerField()
    position = models.IntegerField(
        null=False, blank=False,
        choices = employee_position,
        default = 1
    )

class Orders (models.Model):
    number_client = models.PositiveIntegerField()
    shipping_address = models.CharField(max_length=100)
    order_date = models.DateField()
    number_article = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()





