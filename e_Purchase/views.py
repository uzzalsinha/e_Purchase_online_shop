from django.shortcuts import render
from e_store.models import Product

def home(request):
    items = Product.objects.all()
    return render(request, 'home.html', {'items': items})