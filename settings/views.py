from django.shortcuts import render
from product.models import Brand, Product, Review
from django.db.models.aggregates import Count
# Create your views here.

def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))
    sale_products = Product.objects.filter(flag='Sale')[:10]
    featured_products = Product.objects.filter(flag='Feature')[:6]
    new_products = Product.objects.filter(flag='New')[:10]
    reviews = Review.objects.all()[:5]
    
    context={
        'brands':brands , 
        'sale_products':sale_products , 
        'featured_products': featured_products , 
        'new_products' : new_products , 
        'reviews': reviews
        }
    return render(request,'settings/home.html',context)