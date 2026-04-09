from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Product,Brand
from .serializers import ProductListSerializer, ProductDetailSerializer, BrandListSerializer, BrandDetailSerializer

# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:10]
#     data = ProductListSerializer(products, many=True, context={'request': request}).data
#     return Response({'products': data})

# @api_view(['GET'])
# def product_detail_api(request,pk):
#     products = Product.objects.get(pk=pk)
#     data = ProductDetailSerializer(products,context={'request':request}).data   # json
#     return Response({'product':data})

class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class BrandListAPI(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

class BrandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer