from django.contrib.postgres import serializers
from django.shortcuts import render
from django.http import HttpResponse
from myapp.item.models import Item


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def test(request):
    item = Item.objects.all()
    item_list = serializers.serialize('json', item)
    return HttpResponse(item_list, content_type="text/json-comment-filtered")