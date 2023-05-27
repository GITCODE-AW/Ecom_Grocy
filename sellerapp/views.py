from django.shortcuts import render, redirect
from django.contrib import messages
import sellerapp.models as sellerapp_models

data = {}

def seller_register(request):
    try:
        find_seller = sellerapp_models.seller.objects.get(user=request.user)
    except:
        if request.method == "POST":
            bio = request.POST.get("bio")
            business_name = request.POST.get("business-name")
            business_email = request.POST.get("business-email")
            payment_preference = request.POST.get("payment-preference")

            sellerapp_models.seller.objects.create(user=request.user, bio=bio, business_name=business_name, business_email=business_email, payment_option=payment_preference)
            messages.info(request, 'Congrats.. Now you are seller, check seller panel for more')
            return redirect('sellerapp_panel')

    else:
        # if seller exists. redirect him to panel page..
        messages.info(
            request, "You have already registred as Seller. please continue to panel"
        )
        return redirect("sellerapp_panel")

    data["title"] = "seller registration"
    return render(request, "sellerapp/seller_register.html", data)


def seller_panel(request):
    try:
        find_seller = sellerapp_models.seller.objects.get(user=request.user)
    # if exception occurs then seller does not exists in database. so redirect to seller register page with message 
    except:
        messages.info(request, 'Please Register as Seller to access Panel')
        return redirect('sellerapp_register')
    # this means seller is found and panel should be shown to him
    else:
        data["title"] = "seller pannel"
        return render(request, "sellerapp/seller_panel.html", data)


def seller_products(request):
    try:
        find_seller = sellerapp_models.seller.objects.get(user=request.user)
    # if exception occurs then seller does not exists in database. so redirect to seller register page with message 
    except:
        messages.info(request, 'Please Register as Seller to access Panel')
        return redirect('sellerapp_register')
    # this means seller is found and information shown to him
    else:
        seller = sellerapp_models.seller.objects.get(user=request.user)
        products = seller.products.all()
        data['products'] = products
        data['title'] = "seller's Products"
        return render(request, 'sellerapp/seller_products.html', data)
