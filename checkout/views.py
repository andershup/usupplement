from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings 

from .forms import OrderForm #we need the order forms
from bag.contexts import bag_contents 

import stripe 

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag: #this will prevent people from manually acessing the url by typing /checkout
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request) #we get a python dictionary returned so can display here. current_bag so not overwrite bag.
    total = current_bag['grand_total'] #get the grand total key out of the current bag.
    stripe_total = round(total * 100) #round to zero decimal place since stripe requires the amount to be an integer.
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create( 
    #Create the payment intent giving it the abount and currency
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    
    order_form = OrderForm() #we create an instance of our order form
    template = 'checkout/checkout.html' #we create the template and the context containing the order form
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key, #variables from above
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


