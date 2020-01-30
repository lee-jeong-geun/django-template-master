from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.item import views


#router = DefaultRouter()
#router.register(r'products', views.TempList.as_view())

urlpatterns =[
    #path('products/', ),
    #path('products/<int:pk>')
    path('products/', views.TempList.as_view())
]