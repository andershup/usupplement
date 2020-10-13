from django.shortcuts import render, get_object_or_404
from django.contrib import messages #You dont have messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

@login_required # only logged in users should be able to view this view
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        """creat and instance of the user profile form using post data. Ant tell it the instance we are updating is the profile we have 
        just retrieved above. If form valid we save and add success message"""
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            #this needs to be changed because you dont have messages
            messages.success(request, 'Profile updated successfully')
        else: 
            message.error(request, 'Update failed. Please insure the form is valid.')
    else: #we move the form instantation into an else block so it wont wipe out the form errors
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)

def order_history(request, order_number):
        order = get_object_or_404(Order, order_number=order_number)

        messages.info(request, (
            f'This is a past confirmation for order number {order_number}. '
            'A confirmation email was sent on the order date.'
        ))

        template = 'checkout/checkout_success.html' #same template as checkout
        context = {
            'order': order,
            'from_profile': True, #Variable to check if the user got there via the order history
        }    

        return render(request, template, context)