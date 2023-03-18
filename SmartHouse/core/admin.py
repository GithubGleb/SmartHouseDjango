# Register your models here.
from django.contrib import admin
from .models import New_profile, Controler, Products, CreateAssembling, Assembling, ProductStat
from smarthouseblog.models import Blog

class AssemblingInlie(admin.TabularInline):
    model = Assembling
    extra = 3


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'prod', 'name', 'model', 'condition']
    list_filter = ['condition']
    pass


@admin.register(Controler)
class ControllerAdmin(admin.ModelAdmin):
    list_display = ['id', 'contr', 'model', 'packet']
    list_filter = ['contr', 'packet']
    pass


@admin.register(New_profile)
class New_profileAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'name', 'surname',
                    'username', 'email', 'feedback',
                    'grade']
    list_filter = ['grade']
    pass


@admin.register(CreateAssembling)
class CreateAssemblingAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [AssemblingInlie]
    pass


@admin.register(Assembling)
class AssemblingAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductStat)
class ProductStatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'price']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'title', 'text', 'date', 'date_publication']
