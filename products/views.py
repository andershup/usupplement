from django.shortcuts import render, get_object_or_404
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

def product_detail(request, product_id):
    """ we add product id to parameters  """

    product = get_object_or_404(Product, pk=product_id)
    


    # product singular to return on product with that id.
    context = {
        'product': product,
    # So our products wil be available in the template
    }

    return render(request, 'products/product_detail.html', context)
