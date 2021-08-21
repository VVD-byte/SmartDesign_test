from django.shortcuts import render
from rest_framework import generics

from . import models, serializer


class CreateNewProductView(generics.CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer


class GetNameProductView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer


class GetProductView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
    lookup_field = 'id'
