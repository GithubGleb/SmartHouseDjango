# Register your models here.
from django.contrib import admin
from .models import New_profile, Controler, Products, CreateAssembling, Assembling


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



