from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from myapp.item.models import Product
from myapp.item.serializers import IngredientSerializer, ProductListSerializer, ProductDetailSerializer

# Create your views here.


"""class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    @action()
    def get_list(self, request, *args, **kwargs):
        return Response()
"""


class ProductViewList(APIView):
    pagination_class = PageNumberPagination()

    def get(self, request):
        # get request parameter
        category = request.query_params.get('category')
        ingredient_include_list = request.query_params.get('include')
        ingredient_exclude_list = request.query_params.get('exclude')

        # include_list str to list
        if ingredient_include_list is not None:
            ingredient_include_list = ingredient_include_list.split(',')
        # exclude_list str to list
        if ingredient_exclude_list is not None:
            ingredient_exclude_list = ingredient_exclude_list.split(',')

        products = Product.objects.all()
        if category is not None:
            products = products.filter(category=category)
        if ingredient_include_list is not None:
            for ingredient_include in ingredient_include_list:
                products = products.filter(ingredients=ingredient_include)
        if ingredient_exclude_list is not None:
            for ingredient_exclude in ingredient_exclude_list:
                products = products.exclude(ingredients=ingredient_exclude)

        products_list = []
        querySet_products_list = []

        # skin_type get score
        for product in products:
            score = 0
            for ingredient in product.ingredients.all():
                score += ingredient.calculate_score(skin_type=request.query_params['skin_type'])
            products_list.append((product.id, score, product.price))
        # sort 1) -score 2) price
        products_list.sort(key=lambda t: (-t[1], t[2]))

        for product in products_list:
            querySet_products_list.append(Product.objects.get(id=product[0]))

        results = self.pagination_class.paginate_queryset(querySet_products_list, request)
        serializer = ProductListSerializer(results, many=True)
        return Response(serializer.data)
