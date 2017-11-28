from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
    
def product_details(request, id):
    this_product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product" : this_product}) 
