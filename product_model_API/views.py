from rest_framework import status
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from product_model_API.models import Product

from product_model_API.serializers import (
    ProductSerializer,
    ProductListSerializer,
    ProductUpdateSerializer,
)
from product_model_API.mixins import RetrieveSerializedMixin


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Product created successfully.", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "pk"


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDeleteView(DestroyAPIView, RetrieveSerializedMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized_data = self.get_serialized_object(instance)
        return Response(serialized_data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Product was deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class ProductUpdateView(UpdateAPIView, RetrieveSerializedMixin):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    lookup_url_kwarg = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized_data = self.get_serialized_object(instance)
        return Response(serialized_data)
