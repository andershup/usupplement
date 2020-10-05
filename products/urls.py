from django.urls import path
from . import views
# Note no admin imported as not used


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    # note contains the product id and named product_detail not product
]