from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from demo.models import Productdetails
from demo.serializer import ProductSerializer, serializers


# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = Productdetails.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productdetails
    serializer_class = ProductSerializer
