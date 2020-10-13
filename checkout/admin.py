from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline): #so when see order we get list of editable line items rather than having to go to interface
    model = OrderLineItem
    readonly_fields = ('lineitem_total',) #This is a tuple so read only


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,) #the class above added.

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',     #This fields class is not necessary but allows ordering in admin interface
              'email', 'phone_number', 'country', #we have added user_profile to field the order in the admin
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', #list display option to restrict the columns in the order list.
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',) 

admin.site.register(Order, OrderAdmin) #We skip registering the first class because it is available within this one

