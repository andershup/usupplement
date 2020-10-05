from django.urls import path
from . import views
# Note no admin imported as not used


urlpatterns = [
    path('', views.all_products, name='products')
]