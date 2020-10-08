from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)  #we call the default init method to set up the form as it would be by default
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True #autofocus so cursor start in this field
        for field in self.fields: #we itterate through form fields adding adding a start if required
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *' #adding star
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder #setting all the placeholder att to values in dic above
            self.fields[field].widget.attrs['class'] = 'stripe-style-input' #adding a css class we will use later
            self.fields[field].label = False #removing labels as we now have placeholder set..
            # try this with just the labels .....