from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import Account, Verification
from django.contrib.auth.decorators import login_required
import sellerapp.models as sellerapp_models
from .utils import send_email_token
from . import utils
import uuid


data = {}


# register view
def userapp_register(request):
    if request.method == "POST":
        add_email = request.POST.get("email")
        add_password = request.POST.get("password")
        if add_email and add_password:
            try:
                # check user already exists
                User.objects.get(email=add_email)
            except:
                # means user not present.

                try:
                    # check user present in verification table
                    Verification.objects.get(email=add_email)
                except:
                    # means user not present in verification table and email should be sent
                    new_token = uuid.uuid4()
                    Verification.objects.create(email=add_email, token=new_token)
                    email_sent_status = send_email_token(
                        email=add_email, token=new_token
                    )
                    del new_token
                    if email_sent_status:
                        # email sent
                        messages.info(
                            request,
                            f"Email has been sent on {add_email}. Please check Inbox",
                        )
                    else:
                        messages.info(
                            request,
                            f"Email Could not be sent on {add_email} due to Email either invalid or technical reasons",
                        )
                        return redirect("userapp_register")
                else:
                    # means user present in verification table and message should be sent to him
                    messages.info(
                        request,
                        f"Hello {add_email}, Email already sent to email address. Please check Inbox",
                    )

            else:
                # means user already exists. showing him message
                messages.info(
                    request,
                    f"Hello {add_email}, Your account already exists, please login here",
                )
                return redirect("userapp_login")

    # regular page
    data["title"] = "User Registration Form"
    return render(request, "userapp/userapp_register.html", data)


# verify email view
def userapp_verify(request, uuid):
    if request.method == "POST":
        add_email = request.POST.get("email")
        add_password = request.POST.get("password")
        try:
            Verification.objects.get(email=add_email, token=uuid)
        except:
            messages.info(
                request,
                "user could not be verified due to wrong token. please click on the link in sent email or register again",
            )
            return redirect("userapp_login")
        else:
            Verification.objects.get(email=add_email, token=uuid).delete()
            User.objects.create_user(
                username=add_email, email=add_email, password=add_password
            )
            messages.info(
                request,
                f"Welcome {add_email}, you have been successfully verified. Please Login to Continue",
            )
            return redirect("userapp_login")
    # regular page
    data["title"] = "verify and set password"
    return render(request, "userapp/userapp_verify.html", data)


# login view
def userapp_login(reuqest):
    if reuqest.method == "POST":
        check_email = reuqest.POST.get("email")
        check_password = reuqest.POST.get("password")
        try:
            check_user = User.objects.get(email=check_email)
        except:
            check_user = False

        if check_user:
            authenticated_user = auth.authenticate(
                username=check_email, password=check_password
            )
            if authenticated_user:
                auth.login(reuqest, authenticated_user)
                messages.info(
                    reuqest,
                    f"Welcome {authenticated_user.get_username()}. Please Continue Shopping",
                )
                return redirect("product_home")
            else:
                messages.info(
                    reuqest, f"Hello {check_email}, Please enter correct password "
                )
                return redirect("userapp_login")
        else:
            messages.error(
                reuqest, f"User not found {check_email}. Please egister Here"
            )
            return redirect("userapp_register")
    # regular page
    data["title"] = "User Login"
    return render(reuqest, "userapp/userapp_login.html")


# logout view
@login_required(login_url="userapp_login", redirect_field_name="product_home")
def userapp_logout(request):
    data["title"] = "login page"
    auth.logout(request)
    messages.info(request, "You have been successfully Logged Out. Please visit again")
    return redirect("product_home")


# forgot password - send token view
def userapp_forgot(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # checking if user is registered.
        try:
            find_user = User.objects.get(email=email)
        except:
            messages.error(request, "User Not Found. Please Register")
            return redirect("userapp_forgot_password")
        else:
            # user is present, send him email..., add email and token in database
            try:
                new_token = uuid.uuid4()
                res = utils.send_email_token_forgot(
                    email=find_user.email, token=new_token
                )
            except:
                messages.info(
                    request,
                    f"Hey {find_user.username}, some tech issues occured. please try again later",
                )
                return redirect("userapp_forgot_password")

            else:
                Verification.objects.create(email=find_user.email, token=new_token)
                messages.info(
                    request, f"Hey {find_user.username}, Conformation Sent On Email."
                )
                return redirect('product_home')


    # regular page
    data["title"] = "forgot password"
    return render(request, "userapp/userapp_forgot.html", data)


# forgot password - reset password view
def userapp_reset(request, uuid):
    if request.method == "POST":
        existing_email = request.POST.get('email')
        new_password = request.POST.get('password')
        # check email and uuid present in varification table
        try:
            Verification.objects.get(email=existing_email, token=uuid)
        except:
            messages.info(request, 'User Could Not Be Validated. Please Check Inbox or try again')
            return redirect('userapp_login')
        else:
            find_user = User.objects.get(email=existing_email)
            find_user.set_password(new_password)
            find_user.save()
            Verification.objects.get(email=existing_email, token=uuid).delete()
            messages.info(request, f'hey {find_user.username}, Password Reset Successfull. Please Login')
            return redirect('userapp_login')

    # regular view
    data["title"] = 'reset password'
    return render(request, "userapp/userapp_reset.html", data)

# account panel view for user
@login_required(login_url="userapp_login")
def userapp_account(request):
    data["title"] = "User Account Page"

    # find if user is seller to show him option of go to seller panel
    try:
        find_seller = sellerapp_models.seller.objects.get(user=request.user)
    except:
        data["is_seller"] = False
    else:
        data["is_seller"] = True

    user_account, created = Account.objects.get_or_create(user=request.user)
    if request.method == "POST":
        user_account.state = request.POST.get("state")
        user_account.city = request.POST.get("city")
        user_account.address = request.POST.get("address")
        user_account.phone = request.POST.get("phone")
        user_account.save()
        messages.info(request, "Profile changes has been made..")
        return redirect("userapp_account")
    else:
        data["Account"] = user_account
        return render(request, "userapp/userapp_account.html", data)