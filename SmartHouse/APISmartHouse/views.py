from django.shortcuts import render
from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response
from smarthouseblog.models import Blog, Cart, Order
from .serializers import BlogSerializer, CartSerializer, OrderSerializer


class BlogListViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CartListViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer = CartSerializer(instance=instance)
        return Response(serializer.data)


class OrderListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer



# class OrderList(APIView):
#     def get_list(self, pk):
#         try:
#             order = Order.objects.get(pk=pk)
#             return order
#         except:
#             return Http404
#
#     def get(self, request, pk, format=None):
#         snipet = self.get_list(pk)
#         serializer = OrderSerializer(snipet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snipet = self.get_list(pk)
#         serializer = OrderSerializer(snipet)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, pk, request, format=None):
#         snipet = self.get_list(pk)
#         snipet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class PostList(APIView):
#     def get_list(self, pk):
#         try:
#             return Blog.objects.get(pk=pk)
#         except Blog.DoenNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snipet = self.get_list(pk)
#         serializer = BlogSerializer(snipet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snipet = self.get_list(pk)
#         serializer = BlogSerializer(snipet)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snipet = self.get_list(pk)
#         snipet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)