from django.contrib import admin
from .models import Category, Product, Customer, Order
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'category')
    search_fields = ('name',)
    list_filter = ('category',)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email')
    search_fields = ('full_name', 'email')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product')
    search_fields = ('customer__full_name', 'product__name')
    list_filter = ('customer', 'product')

