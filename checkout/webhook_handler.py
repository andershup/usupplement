from django.http import HttpResponse

#Code from Code Institute
class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event): #will handle the event stripe is sending us
        """
        Handle a generic/unknown/unexpected webhook event
        We use this to handle receive webhooks we are not otherwise handling.
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)