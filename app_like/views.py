from datetime import datetime

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app_like.models import Like
from app_like.serializers import LikeSerializer
from app_products.models import Product
from app_products.serializers import ProductSerializer


class LikeView(GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        likes = Like.objects.filter(user=request.user)
        serializer = self.serializer_class(likes, many=True)
        return Response(serializer.data)

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            product_id = srz_data.validated_data['product_id']
            try:
                Like.objects.get(product__id=product_id, user=request.user)
                return Response({'message': 'this product already liked by you'}, status=status.HTTP_400_BAD_REQUEST)
            except Like.DoesNotExist:
                product = get_object_or_404(Product, pk=product_id, available=True)
                Like.objects.create(user=request.user, product=product, register_date=datetime.now())
                return Response({'message': 'liked success'}, status=status.HTTP_200_OK)



    
# class DisLikeView(GenericAPIView):
    
#     serializer_class = LikeSerializer
#     permission_classes = (
#         IsAuthenticated,
#     )

#     def get(self, request):
#         dislikes = Like.objects.filter(user=request.user)
#         serializer = self.serializer_class(dislikes, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         srz_data = self.serializer_class(data=request.data)
#         if srz_data.is_valid(raise_exception=True):
#             product_id = srz_data.validated_data['product_id']
#             try:
#                 Like.objects.get(product__id=product_id, user=request.user).delete()
#                 return Response({'message': 'like for this produc deleted success'}, status=status.HTTP_200_OK)
#             except Like.DoesNotExist:
#                 return Response({'message': 'you not like this product'}, status=status.HTTP_400_BAD_REQUEST)

