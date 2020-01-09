from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.IntegerField()
    imageId = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    gender = models.CharField(max_length=6)
    category = models.CharField(max_length=10)
    monthlySales = models.IntegerField()