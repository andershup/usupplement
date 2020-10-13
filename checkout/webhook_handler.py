  
#Code copied from Code Institute sizes function removed
from django.http import HttpResponse
from django.core.mail import send_mail #for the send confirmation email 
from django.template.loader import render_to_string #for the send confirmation email
from django.conf import settings # for send confirmation email

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order): #starts with an _ since it will only be used in this class
        """Send the user a confirmation email"""
        cust_email = order.email #we get the customers email from the order
        subject = render_to_string( # see import above
            'checkout/confirmation_emails/confirmation_email_subject.txt', # first param the file we want to render (note subject)
            {'order': order}) # second param is the context we want to pass to the template
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt', #Note: body
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail( #send mail function ( call it below )
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL, #email we want to send from 
            [cust_email] # only going to one email address (although list)
        )        

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

        

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag #the matadata key contains the username of the user that placed the order
        save_info = intent.metadata.save_info #it also contained whether they wanted to save their info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None #set to none so we know we can allow anonynous user to checkout
        username = intent.metadata.username #we can get the username from the metadata. see above
        if username != 'AnonymousUser': #if it is not anonymous user
            profile = UserProfile.objects.get(user__username=username) #we try to get their profile using their username
            if save_info: #If saved box was ticked. we then add default
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()


        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:

            self._send_confirmation_email(order) #paymen has been completed here so we deff want to send conf email
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile, #Since we already have their profile and they were not logged in we can add it to their order when the webhook creates it
                    # In this way the the handler can creat order for both authenticated user, by attaching their profile and anonymour user by setting field to none
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                        
                        )
                    order_line_item.save()
                    
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order) # if the order was created by the webhook handler we send conf email here
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)