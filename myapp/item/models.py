from django.db import models

# Create your models here.
skin_type_map = {'oily': 0, 'dry': 0, 'sensitive': 0}
score_map = {'O': 1, 'X': -1, '': 0}


class Ingredient(models.Model):
    name = models.CharField(auto_created=False, primary_key=True, max_length=40)
    oily = models.CharField(max_length=1)
    dry = models.CharField(max_length=1)
    sensitive = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    def calculate_score(self, skin_type):
        skin_type_map['oily'] = score_map[str(self.oily)]
        skin_type_map['dry'] = score_map[str(self.dry)]
        skin_type_map['sensitive'] = score_map[str(self.sensitive)]
        return skin_type_map[skin_type]


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    imageId = models.CharField(max_length=40)
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    gender = models.CharField(max_length=6)
    category = models.CharField(max_length=10)
    ingredients = models.ManyToManyField(Ingredient, related_name='product_ingredient')
    monthlySales = models.IntegerField()
