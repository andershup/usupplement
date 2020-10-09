from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings 

from .forms import OrderForm #we need the order forms
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_contents 

import stripe 

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST': #from our payment submit button
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data) #instance of the form using the form data
        if order_form.is_valid(): 
            order = order_form.save() #to get the order number for line 48 checkout success
            for item_id in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                        )
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number])) #pass the order number as an argument for the url

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')


    else: #to handle the GET request

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


def checkout_success(request, order_number):
    """
    Lets user know their payment is complete
    """
    #find out if the user ticked to save info 
    save_info = request.session.get('save_info') 
    order = get_object_or_404(Order, order_number=order_number) #same as order number line 85
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    #delete the users shopping bag since it will no longer be needed or this session
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    #render template
    return render(request, template, context)
