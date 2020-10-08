from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm #we need the order forms


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag: #this will prevent people from manually acessing the url by typing /checkout
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm() #we create an instance of our order form
    template = 'checkout/checkout.html' #we create the template and the context containing the order form
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


