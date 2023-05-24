from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BlogListViewSets, CartListViewSet, OrderListViewSet


route = DefaultRouter()
route.register('ApiBlog', BlogListViewSets, basename='BlogListViewSets')
route.register('Cart', CartListViewSet, basename='CartListViewSet')
route.register('Order', OrderListViewSet, basename='OrderListViewSet')

urlpatterns = [
    path('', include(route.urls)),
]