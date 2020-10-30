from django.urls import path
from . import views
# Note no admin imported as not used


urlpatterns = [
    path('', views.all_products, name='products'),
    # the int is added to prevent the following paths being interpreted as a string.
    path('add/', views.add_product, name='add_product'),
    #no template requred just a view and url
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('summary<int:product_id>/', views.summary, name='summary'), 
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]