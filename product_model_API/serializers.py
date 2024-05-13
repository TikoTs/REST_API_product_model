from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from product_model_API.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]


class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["supply"]
