from django.contrib.postgres import serializers
from django.shortcuts import render
from django.http import HttpResponse
from myapp.item.models import Item


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def test(request):
    item_list = Item.objects.all()
    str = ''
    for i in item_list:
        str += "<p>id : {}<br>imgid : {}<br>name : {}<br>price : {}<br>monthlySales : " \
               "{}<br></p>".format(i.id, i.imageId, i.name, i.price, i.monthlySales)
    return HttpResponse(str)