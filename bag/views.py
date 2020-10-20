from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from products.models import Product
# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id) #For showing message "success" below.
    quantity = int(request.POST.get('quantity')) # First thing is to get the quantity from the form. int cause it comes as a string.
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {product.name} to your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag', {})
    try:
        bag.pop(item_id)
        messages.info(request, f'Removed {product.name} from your bag')  
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
    