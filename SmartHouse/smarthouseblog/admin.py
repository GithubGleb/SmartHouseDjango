from django.contrib import admin
from .models import Blog, Comments, Category, Cart, Order


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'title', 'category', 'text', 'date', 'date_publication', 'status', 'raiting',
                    'price', ]
# Register your models here.


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'username', 'date', 'comment', 'raiting']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['item']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'date_order', 'date_dilivery', 'total_price']
