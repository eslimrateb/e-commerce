from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics ,filters
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
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['brand','flag']
    search_fields = ['name','description','brand__name']
    ordering_fields = ['price','quantity']
    #ordering=['brand__name']  # default ordering

class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class BrandListAPI(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

class BrandDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer