from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Brand, Review
from django.db.models import  Q, F, Value, Count
from django.db.models.aggregates import Sum, Avg, Min, Max
# Create your views here.
class ProductList(ListView):
    model = Product
    paginate_by = 30

class ProductDetail(DetailView):
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(product=self.get_object())
        context["related_products"] =Product.objects.filter(brand=self.get_object().brand)
        return context
    
class BrandDetail(ListView):
    model = Product
    paginate_by = 10
    template_name = 'product/brand_detail.html'
    def get_queryset(self):
         brand=Brand.objects.get(slug=self.kwargs['slug'])
         return super().get_queryset().filter(brand=brand)
  
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['brand']= Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
      return context
  
class BrandList(ListView):
    model = Brand
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
    paginate_by = 30


    
def queryset_debug(request):

    data = Product.objects.select_related('brand').all() # prefetch_related = many-to-many
    # filter 
    # data = Product.objects.filter(price__gt= 70)
    # data = Product.objects.filter(price__gte= 70)
    # data = Product.objects.filter(price__lt= 70)
    # data = Product.objects.filter(price__lte= 70)
    # data = Product.objects.filter(price__range= (60,70))
    
    # navigate relation
    # data = Product.objects.filter(brand__name='Apple')
    # data = Product.objects.filter(brand__price__gt=20)
    
    # filter with text
    # data = Product.objects.filter(name__contains='Brown')
    # data = Product.objects.filter(name__startswith='Grac')
    # data = Product.objects.filter(name__endswith='Love')
    # data = Product.objects.filter(name__endswith='Love')
    # data = Product.objects.filter(tags__isnull=True)
    
    # filter date time
    # data = Review.objects.filter(created_at__year=2023)
    # data = Review.objects.filter(created_at__month=2023)
    
    # filter 2 values
    # data = Product.objects.filter(price__gt=80 , quantity__lt=10)  # and 
    # data = Product.objects.filter(
    #     Q(price__gt=80) |
    #     Q(quantity__lt=10)
    #     )  # or

    # data = Product.objects.filter(
    #     Q(price__gt=80) &
    #     Q(quantity__lt=10)
    #     )  # or
    
    # data = Product.objects.filter(
    #     Q(price__gt=80) &
    #     ~Q(quantity__lt=10)
    #     )  # or with not 
    
    # field lookup
    # data = Product.objects.filter(price=F('quantity'))
    
    
    
    # data = Product.objects.all().order_by('name')  # ASC
    # data = Product.objects.order_by('name')    # ASC
    # data = Product.objects.order_by('-name')   # DES
    # data = Product.objects.order_by('name').reverse()   # DES
    # data = Product.objects.order_by('name','quantity')
    # data = Product.objects.order_by('name','-quantity')
    
    # data = Product.objects.order_by('name')[0]  # first
    # data = Product.objects.order_by('name')[-1] # last   
    # data = Product.objects.earliest('name')  # first
    # data = Product.objects.latest('name') # last 
    
    # slice
    # data = Product.objects.all()[10:20]
    
    # select columns
    # data = Product.objects.values('name','price')
    # data = Product.objects.values('name','price','brand__name')
    # data = Product.objects.values_list('name','price','brand__name')
    
    # remove duplicate
    # data = Product.objects.all().distinct()
    
    
    # data = Product.objects.only('name','price')
    # data = Product.objects.defer('slug','description')
    
    # aggregation 
    # data = Product.objects.aggregate(Sum('quantity'))
    # data = Product.objects.aggregate(Avg('price'))
    
    # annotate 
    # data = Product.objects.annotate(price_with_tax=F('price')*1.2)
    # data = Product.objects.aggregate(total_price=Sum('price',filter=Q(price__gt=50)))
    
    # annotate with aggregation to each row summery of reviews for each product
    # data = Product.objects.annotate(total_reviews=Count('review'))

    return render(request,'product/debug.html',{'data':data})