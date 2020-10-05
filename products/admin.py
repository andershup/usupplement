from django.contrib import admin
from .models import Product, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    """Class which will extend the built in model admin class"""
    list_display = (
    # List display attribute as a tuple to tell admin which fields to display
    # Column order in admin can be changed here
        'name',
        'category',
        'sku',
        'price',
        'rating',
        'image',
    )
    # Ordering attribute tuple to sort by 'sku'
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """Class which will extend the built in model admin class"""
    list_display = (
    # List display attribute as a tuple to tell admin which fields to display
        'name',
        'friendly_name',
    )

# Category and Classes registration
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)