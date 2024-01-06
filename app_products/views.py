from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

from datetime import datetime
from .permissions import IsSellerOfProduct

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        products = request.user.store.products.all()
        srz_data = self.serializer_class(instance=products, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


# Представление для получения деталей, обновления и удаления продукта
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = IsSellerOfProduct
