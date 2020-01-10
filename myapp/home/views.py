from django.contrib.postgres import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from myapp.item.models import Item


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def test(request):
    item = Item.objects.filter(published_at__isnull=False).order_by('-published_at')
    item_list = serializers.serialize('json', item)
    return HttpResponse(item_list)