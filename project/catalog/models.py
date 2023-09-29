from django.db import models
from django.db.models import F


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()


class Basket(models.Model):
    quantity = models.IntegerField()
    total_price = F('Item.price') * F('quantity')

