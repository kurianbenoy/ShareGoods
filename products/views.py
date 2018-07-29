from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import Product,ProductCondition
from .filters import ProductFilter

from .serializers import ProductSerializer,ProductConditionSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductConditionList(generics.ListCreateAPIView):
    queryset = ProductCondition.objects.all()
    serializer_class = ProductConditionSerializer

class ProductConditionDetail(generics.RetrieveUpdateAPIView):
    queryset = ProductCondition.objects.all()
    serializer_class = ProductConditionSerializer

# def search(request):
    # product_list = Product.objects.all()
    # product_filter = ProductFilter(request.GET,queryset=product_list)
    # return JsonResponse({'search':product_filter})

class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title','category__category','description','subcategory__subcategory',)
    # filter_class = ProductFilter
