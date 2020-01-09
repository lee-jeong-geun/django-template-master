from django.shortcuts import render
from django.http import HttpResponse
from myapp.item.models import Item


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def test(request):
    return render(request, 'test.html', {})