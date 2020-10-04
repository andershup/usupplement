from django.shortcuts import render

# Create your views here.
def index(request):
    """View for index page (or might be one of many)"""

    return render(request, 'home/index.html')