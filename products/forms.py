from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__' # dunder that will include all the fields
    #replacing the image field with the new one which utilizes the widget
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs): # we override the init method to make a few changes to the field
        super().__init__(*args, **kwargs)
        categories = Category.objects.all() #get all the categories
        #Create a list of tuples associated with their category ids
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories] # list comprehension syntax
        # use friendly names instead of id
        self.fields['category'].choices = friendly_names
        #itterate and add classes to match the rest of the store
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'