from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe


#Code copied from stripe and Code Institute
@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        print('first') 
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('second') #This one causing the error
        print(wh_secret)
        return HttpResponse(status=400)
    except Exception as e:
        print('third')
        return HttpResponse(content=e, status=400)

    # Code from Code Institute
    # Set up a webhook handler
    handler = StripeWH_Handler(request) #creating an instance passing in request

    # Map webhook events to relevant handler functions
    # We create  a dic and the keys will be the names of the webhooks coming from stripe
    # and the values will be the actual methods inside the handler
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type'] # payment failed/ succeeded etc.
    # Once we get the type we look it up in the key dictionary and assign it to a variable
    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)
    # envent_handler is just an alias for whatever function we pulled out of the dictionary
    # Call the event handler with the event
    response = event_handler(event)
    print('forth')
    return response

    
