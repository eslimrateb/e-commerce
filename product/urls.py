from django.urls import path
from .views import BrandDetail, BrandList, ProductList, ProductDetail, queryset_debug

urlpatterns = [
    path('', ProductList.as_view()),
    path('debug',queryset_debug),
    path('brands/', BrandList.as_view()),
    path('<slug:slug>/', ProductDetail.as_view()),
    path('brands/<slug:slug>/', BrandDetail.as_view()),
    
]