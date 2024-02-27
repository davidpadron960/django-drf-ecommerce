from producto.models import Producto,Categoria
from producto.api.serializers import ProductoSerializer,CategoriaSerializer
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

"""
@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products = Producto.objects.all()
        serializer = ProductoSerializer(products,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    if request.method == 'GET':
        try:
             products = Producto.objects.get(pk=pk)
             serializer = ProductoSerializer(products)
             return Response(serializer.data)
        except Producto.DoesNotExist:
            return Response({'Error': 'El Producto no existe'},status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
         products = Producto.objects.get(pk=pk)
         serializer = ProductoSerializer(products,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        try:
            products = Producto.objects.get(pk=pk)
            products.delete()
        except Producto.DoesNotExist:
            return Response({'Error': 'El Producto no existe'},status=status.HTTP_404_NOT_FOUND)
        return Response({'mensaje': 'Producto eliminado correctamente'},status=status.HTTP_200_OK)
"""

class ProductListAV(APIView):

    def get(self,request):
        products = Producto.objects.all()
        serializer = ProductoSerializer(products,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAv(APIView):

    def get(self,request,pk):
        products = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(products)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        products = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(products,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        products = Producto.objects.get(pk=pk)
        products.delete()
        return Response({'mensaje':'Producto eliminado correctamente'},status=status.HTTP_200_OK)

class CategoriaAV(APIView):
    def get(sel,request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAv(APIView):

    def get(self,request,pk):
        categorias = Producto.objects.get(pk=pk)
        serializer = CategoriaSerializer(categorias)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        categorias = Categoria.objects.get(pk=pk)
        serializer = CategoriaSerializer(categorias,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        categorias = Categoria.objects.get(pk=pk)
        categorias.delete()
        return Response({'mensaje':'Categoria eliminada correctamente'},status=status.HTTP_200_OK)

    
