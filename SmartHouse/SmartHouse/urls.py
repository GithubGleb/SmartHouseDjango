"""SmartHouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from core.views import index, paginationproduct, add_product, get_all_profile, ProductView, ProductsView, CommentsViewSet, infouser
from rest_framework.routers import DefaultRouter

r = DefaultRouter()
r.register('comments', CommentsViewSet)


urlpatterns = [
    path('index/', index),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view()),
    path('profile/', infouser),
    path('product/', paginationproduct),
    path('add_product/', add_product),
    path('accounts/profile/', include('core.urls')),
    path('all_list/', get_all_profile),
    path('api/productinfo/v1/', ProductsView.as_view()),
    path('api/productinfo/v1/<pk>/', ProductView.as_view()),
    path('', include('smarthouseblog.urls')),
    path('', index),
] + r.urls
