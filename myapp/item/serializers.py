from rest_framework import serializers
from .models import Ingredient, Product


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['name']


class ProductListSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer

    class Meta:
        model = Product
        fields = ['id', 'imageId', 'name', 'price', 'ingredients', 'monthlySales']


class ProductDetailSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer

    class Meta:
        model = Product
        fields = ['id', 'imageId', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales']