# 백엔드 프론트엔드 연결

# 장고 시작 
pip install django-rest-framework

rom django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  
  from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductList(APIView):
  def get(self, request):
    products = Product.objects.all()
    return Response(products.to_json())
  
  
