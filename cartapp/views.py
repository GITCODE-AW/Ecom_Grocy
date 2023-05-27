from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages

data = {}


def cartapp_cart(request):
    if request.method == "GET":
        add_one = request.GET.get("add_one")
        subtract_one = request.GET.get("subtract_one")
        remove_one = request.GET.get("remove_one")
        item_id = request.GET.get("product_id")

        if item_id:
            get_item = models.Cartitems.objects.get(id=item_id)

            if add_one is not None:
                get_item.quantity += 1
                get_item.save(update_fields=["quantity"])

            elif subtract_one is not None:

                if get_item.quantity == 1:
                    get_item.delete()
                elif get_item.quantity > 1:
                    get_item.quantity -= 1
                    get_item.save(update_fields=["quantity"])

            elif remove_one is not None:
                get_item.delete()

            return redirect("cartapp_cart")

    # regular view
    cart = models.Cart.objects.all()
    cart_items = models.Cartitems.objects.all()
    data["cart_items"] = cart_items
    data["cart"] = cart
    data["title"] = "Cart"
    return render(request, "cartapp/cartapp_cart.html", data)

@login_required(login_url='userapp_login')
def cartapp_order(request):
    if request.method == "GET":
        place_order = request.GET.get('place_order')
        if place_order == 'True':
            cart_instance = models.Cart.objects.get(user = request.user)
            cart_item_instance = models.Cartitems.objects.filter(cart_id=cart_instance.id)

            for item in cart_item_instance:
                models.Order.objects.create(cart_id=cart_instance,user=request.user, product_id=item.product.id, quantity=item.quantity)
                models.Cartitems.objects.get(cart_id=cart_instance.id).delete()
                

            messages.info(request, 'Order is placed')
            return redirect('cartapp_cart')

            
    messages.info(request, 'No order is placed')
    return redirect('cartapp_cart')
