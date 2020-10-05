from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q #special model from django to generate a search query with 'or' logic
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products on home page """

    
    products = Product.objects.all()
    # To return all products from the database
    query = None
    #copied for Code Institute lesson
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!") #change this
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) #we want the query to match eithe in name or description so use q
            products = products.filter(queries)

    context = {
        'products': products,
    # So our products wil be available in the template
        'search_term': query,
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
