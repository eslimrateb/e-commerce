from rest_framework import serializers
from .models import Product , Brand, Review
from taggit.serializers import TagListSerializerField,TaggitSerializer


class ProductListSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    avg_rate2 = serializers.FloatField(source='avg_rate', read_only=True)
    avg_rate = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    price_with_taix=serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    def get_avg_rate(self, product:Product):
        return product.avg_rate()
    def get_review_count(self, product:Product):
        return product.review_product.count()
    def get_price_with_taix(self,product:Product):
        return product.price*1.23
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class ProductDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    reviews = ReviewSerializer(source='review_product',many=True)
    tags = TagListSerializerField()
    class Meta:
        model = Product
        fields = '__all__'

class BrandListSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source='product_brand',many=True)

    class Meta:
        model = Brand
        fields = '__all__'

class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source='product_brand',many=True)
    product_count=serializers.SerializerMethodField()
    class Meta:
        model = Brand
        fields = '__all__'
    def get_product_count(self,brand:Brand):
        return brand.product_brand.count()
