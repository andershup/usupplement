from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
# so when see order we get list of editable line items rather than having to go to interface


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid')
    # This fields class is not necessary but allows ordering in admin interface
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              # we have added user_profile to field the order in the admin
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 'stripe_pid')
    # list display option to restrict the columns in the order list.
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    # putting the  most recent orders at the top
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
