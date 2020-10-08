  
from django.db.models.signals import post_save, post_delete #so these signals are sent to entire application after model instance is saved/deleted
from django.dispatch import receiver #importing the signal receiver

from .models import OrderLineItem # because we will be listening to the signal from the orderlineitem so we need that imported as well

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs): # sender is the order line item
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total() # we access the instance.order (specific to this) and call updatetotal method on it

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs): #the 'create' as above is removed bacause this is not sent by this signal
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()