from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    # Set initial values to 0
    bag_items = []
    total = 0
    product_count = 0
    # Get the bag from the session
    bag = request.session.get('bag', {})

    # Itterate through bag
    for item_id, quantity in bag.items():
        # 404 if no item_id
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Calculate delivery cost. (Standard set in settings.py)
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
