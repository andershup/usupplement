"""Telling django the name of the default config class for the app (in apps.py)
Without this line django would not know about the custom ready method so our 
signals would not work"""
default_app_config = 'checkout.apps.CheckoutConfig'