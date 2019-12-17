from django.shortcuts import render
from .models import Product
# Create your views here.
def list_products(request):
    products = Product.objects.all() 
    return render(request,'index.html',{'products': products})


def detail_product(request,pk):
    product = Product.objects.get(pk=pk) 
    return render(request,'detail.html',{'product': product})


