from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Brand,Category,Product
from .serializers import CategorySerializer,BrandSerializer,ProductSerializer

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    """
    a simple viewset for viewing categories
    """
    queryset = Category.objects.all()

    def list(self,request):
        serializer = CategorySerializer(self.queryset,many=True)
        return Response(serializer.data)

