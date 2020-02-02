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

        if category is None:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category=category)
        products_list = []
        sort_products_list = []

        # skin_type get score
        for product in products:
            score = 0
            for ingredient in product.ingredients.all():
                score += ingredient.calculate_score(skin_type=request.query_params['skin_type'])
            products_list.append((product.id, score, product.price))
        # sort 1) -score 2) price
        products_list.sort(key=lambda t: (-t[1], t[2]))

        for product in products_list:
            delete_product = False
            ingredient_list = Product.objects.get(id=product[0]).ingredients.all()
            # ingredient_include check
            if ingredient_include_list is not None:
                for ingredient_include in ingredient_include_list:
                    exist = False
                    for ingredient_list_val in ingredient_list:
                        if ingredient_include == str(ingredient_list_val):
                            exist = True
                    if not exist:
                        delete_product = True

            # ingredient_exclude check
            if ingredient_exclude_list is not None:
                for ingredient_exclude in ingredient_exclude_list:
                    exist = False
                    for ingredient_list_val in ingredient_list:
                        if ingredient_exclude == str(ingredient_list_val):
                            exist = True
                    if exist:
                        delete_product = True
            if not delete_product:
                sort_products_list.append(Product.objects.get(id=product[0]))

        results = self.pagination_class.paginate_queryset(sort_products_list, request)
        serializer = ProductListSerializer(results, many=True)
        return Response(serializer.data)
