"""
from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto
# Create your views here.

def product_list(request):
    products = Producto.objects.all()
    data = {
        'products':list(products.values())
    }
    return JsonResponse(data)

def product_detail(request,pk):
    products = Producto.objects.get(pk=pk)
    data = {
        'name':products.name,
        'description':products.description,
        'price': products.price,
        'active':products.active,
    }
    return JsonResponse(data)
"""