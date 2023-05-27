from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from cartapp import models as cartapp_models
from django.contrib import messages

data = {}

def product_home(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')

        if product_id is not None:
            find_product = Product.objects.get(id=product_id)
            try:
                find_cart, create_cart = cartapp_models.Cart.objects.get_or_create(user=request.user)
            except:
                messages.info(request, 'Please Login In Order To Access Cart')
            else:
                try:
                    cartapp_models.Cartitems.objects.get(product=product_id)
                except:
                    cartapp_models.Cartitems.objects.create(product=find_product, cart=find_cart)
                else:
                    messages.info(request, 'Product Already Exists On Cart')

                return redirect('product_home')

    products = Product.objects.all()
    data['products'] = products
    data['title'] = "products home"

    if request.method == 'GET':
        searched_product = request.GET.get('searched_product')
        if searched_product:
            products = Product.objects.filter(product_name__icontains=searched_product)
            if products:
                data['products'] = products
                
    # regular page
    return render(request, 'productapp/product_home.html', data)

def product_specific(request, product_id):
    product = Product.objects.get(id=product_id)
    data['product'] = product
    return render(request, 'productapp/product_specific.html', data)