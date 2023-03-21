from django.contrib import admin
from .models import Blog, Comments, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'title','category', 'text', 'date', 'date_publication', 'status', 'raiting']
# Register your models here.


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'username', 'date', 'comment', 'raiting']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['item']

