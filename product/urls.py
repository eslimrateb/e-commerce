from django.urls import path
from .views import BrandDetail, BrandList, ProductList, ProductDetail, queryset_debug
from .api import ProductListAPI, ProductDetailAPI,BrandDetailAPI,BrandListAPI
urlpatterns = [
    path('', ProductList.as_view()),
    path('debug',queryset_debug),
    path('brands/', BrandList.as_view()),
    path('<slug:slug>/', ProductDetail.as_view()),
    path('brands/<slug:slug>/', BrandDetail.as_view()),
    path('api/list', ProductListAPI.as_view()),
    path('api/list/<int:pk>/', ProductDetailAPI.as_view()),
    path('brands/api/list', BrandListAPI().as_view()),
    path('brands/api/list/<int:pk>/', BrandDetailAPI.as_view()),
    
]