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
        str += "<p>{} name {}age<br></p>".format(i.name, i.age)
    return HttpResponse(str)