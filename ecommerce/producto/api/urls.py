from django.urls import path 
#from producto.api.views import product_list,product_detail
from producto.api.views import ProductListAV,ProductDetailAv,CategoriaAV,CategoryDetailAv

urlpatterns = [
    path('list/',ProductListAV.as_view(),name='product_list'),
    path('list/<int:pk>/',ProductDetailAv.as_view(),name='product_detail'),
    path('category/',CategoriaAV.as_view(),name='category'),
    path('category/<int:pk>',CategoryDetailAv.as_view(),name='category-datail'),
]