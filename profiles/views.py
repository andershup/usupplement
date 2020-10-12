from django.shortcuts import render, get_object_or_404
from django.contrib import messages #You dont have messages

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

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

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)