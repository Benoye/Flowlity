from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    inventory = models.IntegerField()


class ProductInventory(models.Model):
    product = models.ForeignKey(Product, on_delete='')
    date = models.DateTimeField()
    inventory = models.IntegerField()
