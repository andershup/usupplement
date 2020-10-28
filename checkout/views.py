from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages #you dont have messages
from django.conf import settings 

from .forms import OrderForm #we need the order forms
from .models import Order, OrderLineItem

from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents 

import stripe 
import json

@require_POST
def cache_checkout_data(request):
    """ Before the confirm card payment is called in the JS we will make 
    a post request to the view and give it the client secret key"""
    try:
        # we split at the word secret so the first part will be the payment intent id, stored in pid
        pid = request.POST.get('client_secret').split('_secret')[0]
        # set up stripe with the secret key so we can modify the payment intent
        stripe.api_key = settings.STRIPE_SECRET_KEY
        #to do this we call modify on paymentintent. give it the pid and add our metadata bolow:
        stripe.PaymentIntent.modify(pid, metadata={ 
            # Add json dump of user shopping bag
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    """ A view for handling payment submit """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    for item_id in bag:
        print(item_id)
    if request.method == 'POST': 
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
        # Instance of the form using the form data
        order_form = OrderForm(form_data) 
        if order_form.is_valid(): 
            # Save the order and commit False to avoid multiple commits
            order = order_form.save(commit=False) 
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save() 
            for item_id, item_data in bag.items():
                print(item_id)
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=item_data,
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
            #pass the order number as an argument for the url
            return redirect(reverse('checkout_success', args=[order.order_number])) 

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')


    else: 
             #this will prevent people from manually acessing the url by typing /checkout
            bag = request.session.get('bag', {})
            if not bag:
                messages.error(request, "There's nothing in your bag at the moment")
                return redirect(reverse('products'))
            #we get a python dictionary returned so can display here. current_bag so not overwrite bag.
            current_bag = bag_contents(request) 
            total = current_bag['grand_total']
            # round to zero decimal place since stripe requires the amount to be an integer 
            stripe_total = round(total * 100) 
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create( 
            #Create the payment intent giving it the amount and currency
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

            if request.user.is_authenticated:
                #prefill user form 
                try: 
                    profile = UserProfile.objects.get(user=request.user)
                    order_form = OrderForm(initial={
                        'full_name': profile.user.get_full_name(),
                        'email': profile.user.email,
                        'phone_number': profile.default_phone_number,
                        'country': profile.default_country,
                        'postcode': profile.default_postcode,
                        'town_or_city': profile.default_town_or_city,
                        'street_address1': profile.default_street_address1,
                        'street_address2': profile.default_street_address2,
                        'county': profile.default_county,
                    })
                #if not authenticated render empty form 
                except UserProfile.DoesNotExist:
                    order_form = OrderForm() 
            else:
                order_form = OrderForm()

            
            
            #we create the template and the context containing the order form
            template = 'checkout/checkout.html' 
            context = {
                'order_form': order_form,
                'stripe_public_key': stripe_public_key, 
                'client_secret': intent.client_secret,
            }

            return render(request, template, context)


def checkout_success(request, order_number):
    """
    Lets user know their payment is complete
    """
    #find out if the user ticked to save info 
    save_info = request.session.get('save_info') 
    order = get_object_or_404(Order, order_number=order_number) 

    if request.user.is_authenticated: 
        #without this if statement it would break payments for anonymous users
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            #we create an instance of the user profile form usng the profile data telling it we are going to update the profile we have obtained above
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()    

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
    return render(request, template, context)
