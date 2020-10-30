from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save #used in the reciever
from django.dispatch import receiver #For the signal to work

from django_countries.fields import CountryField

# Create your models here.

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # delivery fields we want the user to be able to provide defaults
    # these can come directly from the order model and we want all fields to be optional
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Adding the receiver for the post save envent from the user model. Since there is only one signal we are not putting it in a seperate signals.py module like 
    we did with the other ones in the order model
    """
    if created:
        UserProfile.objects.create(user=instance)
    #Existing users: just save the profile
    instance.userprofile.save()