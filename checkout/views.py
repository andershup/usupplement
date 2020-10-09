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
        'stripe_public_key': 'pk_test_51HTj2cCi7YLtVGm0pWL4D5Q5sk08Gh2knTN9EGqcxOhDfs9TAqwWi3Cle4HHsDyQoOg843xbuar1vub2G810qMCQ00s6p7kIym',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)


