from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.item.models import Product, Ingredient
from myapp.item.serializers import IngredientSerializer, ProductListSerializer, ProductDetailSerializer
# Create your views here.


def get_skin_score(product, skin):
    totalScore = 0
    ingredient_list = product.ingredients.all()
    for i in ingredient_list:
        if Ingredient(i, skin) == "O":
            totalScore += 1
        elif Ingredient(i, skin) == "X":
            totalScore -= 1
    return totalScore


"""class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    @action()
    def get_list(self, request, *args, **kwargs):
        return Response()
"""


class TempList(APIView):

    def get(self, request):
        products = Product.objects.all()
        print("Hy")
        ###
        ### sorting ###
        ###
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


