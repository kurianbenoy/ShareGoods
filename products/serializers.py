from rest_framework import serializers
from .models import Product,ProductCondition

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

class ProductConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCondition
        fields =('__all__')
