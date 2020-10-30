from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# because we will be listening to the signal from the orderlineitem
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
# sender is the order line item
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)

def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    # print('delete signal received!!!') used to test signal
    instance.order.update_total()
