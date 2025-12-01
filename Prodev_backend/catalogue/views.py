from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
# Create your views here.



class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.select_related('category').all()
   serializer_class = ProductSerializer
   filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
   filterset_fields = ['category', 'available']
   search_fields = ['title', 'description', 'sku']
   ordering_fields = ['price', 'created_at', 'inventory']


   def get_queryset(self):
      qs = super().get_queryset()
      return qs


class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   lookup_field = 'slug'