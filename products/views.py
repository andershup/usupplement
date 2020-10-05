from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products on home page """

    products = Product.objects.all()
    # To return all products from the database
    context = {
        'products': products,
    # So our products wil be available in the template
    }

    return render(request, 'products/products.html', context)

    