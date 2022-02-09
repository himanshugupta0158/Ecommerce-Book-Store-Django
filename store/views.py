from pyexpat import model
from re import template
from django.shortcuts import render , get_object_or_404
from .models import Category, Product


# adding below function view to setting to make it avaiable in whole project
def categories(request):
    return {'categories' : Category.objects.all()}

    
def all_products(request):
    product_list = Product.objects.all()
    return render(request , 'store/home.html' , {'product_list':product_list})
        

def product_detail(request , slug):
    product = get_object_or_404(Product , slug=slug , in_stock = True)
    
