from django.urls import path
from . import views
# Note no admin imported as not used


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'), #the / is just good practice
    # we have had to update the above with a int: to specidy id should be an int since otherwise navigation to products /add will interpret the 
    # string add as a product id because django will always the first URL it finds a matching pattern for and in this case unless we specify that product id is
    # an integer django does not know the fifference between a product number an da string like add
    # note contains the product id and named product_detail not product
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'), #no template requred just a view and url
]