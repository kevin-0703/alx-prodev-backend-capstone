from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
   class Meta:
       model = Category
       fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
       write_only=True, queryset=Category.objects.all(), source='category'
    )


    class Meta:
       model = Product
       fields = [
           'id','sku','title','slug','description','price','available','inventory',
           'category','category_id','created_at','updated_at'
     ]
       read_only_fields = ['id','created_at','updated_at']


    def create(self, validated_data):
       return super().create(validated_data)


    def update(self, instance, validated_data):
       return super().update(instance, validated_data)