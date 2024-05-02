from rest_framework import status
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from product_model_API.models import Product

from product_model_API.serializers import (
    ProductSerializer,
    ProductListSerializer,
    ProductUpdateSerializer,
)


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {"message": "Product created successfully."},
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        return Response(
            {"error": "Unable to create the product."},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "pk"


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDeleteView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        product.delete()
        return Response(
            {"message": "Product was deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    lookup_url_kwarg = "pk"
