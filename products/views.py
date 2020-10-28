from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# below is imported to stop users from adding/deleting products by using the correct /uls
from django.contrib.auth.decorators import login_required
from django.db.models import Q #special model from django to generate a search query with 'or' logic
from .models import Product,Category
from .forms import ProductForm
# Create your views here.


def all_products(request):
    """ A view to show all products on home page """

    products = Product.objects.all()
    # To return all products from the database
    query = None
    categories = None
    sort = None
    direction = None 
    #copied for Code Institute lesson
    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',') # you dont need to split at the commas I dont think(not comma seperated in main-nav)
            products = products.filter(category__name__in=categories) #note double underscore for django query (looking for nameField of the category model)
            categories = Category.objects.filter(name__in=categories) # and we can do this because cat and product are related with a foreign key.

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!") #change this
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) #we want the query to match eithe in name or description so use q
            products = products.filter(queries)
            if not products:
                messages.error(request, "Sorry we do not have that product")

    context = {
        'products': products,
    # So our products wil be available in the template
        'search_term': query,
        'current_categories': categories,
         #we name the list of category objects and return it to the context so we can use in template later on.
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ we add product id to parameters  """

    product = get_object_or_404(Product, pk=product_id)
    


    # product singular to return on product with that id.
    context = {
        'product': product,
    # So our products wil be available in the template
    }

    return render(request, 'products/product_detail.html', context)

@login_required # imported above. django will check if user is logged in first before executing the view
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required    
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id) #prefilling the form 
    if request.method == 'POST': #the press to update post
        form = ProductForm(request.POST, request.FILES, instance=product) #instanciating the product form using the forms and we tell it the specific instance 
        # we would like to update (the product obtained aboves)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id): 
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))