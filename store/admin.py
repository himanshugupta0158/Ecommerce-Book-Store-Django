from django.contrib import admin

from .models import Category, Product

# Registering Models with additional information


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # prepopulating slug field whenever we populated name field
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'slug', 'price', 'in_stock',
        'created', 'updated'
    ]
    list_filter = ['in_stock', 'is_active', ]
    # allow some fields to be editable even not even need to go to option.
    list_editable = ['price', 'in_stock' ,]
    prepopulated_fields = {'slug': ('title',)}
