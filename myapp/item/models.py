from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(auto_created=False, primary_key=True, max_length=40)
    oily = models.CharField(max_length=1)
    dry = models.CharField(max_length=1)
    sensitive = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    def __str__(self, type):
        if type == "oily":
            return self.oily
        elif type == "dry":
            return self.dry
        return self.sensitive


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    imageId = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    gender = models.CharField(max_length=6)
    category = models.CharField(max_length=10)
    ingredients = models.ManyToManyField(Ingredient, related_name='product_ingredient')
    monthlySales = models.IntegerField()

