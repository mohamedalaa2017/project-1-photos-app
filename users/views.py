from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


from django.apps import apps


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    else:
        return render(request, "users/user.html")
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {
                "massage": 'invalid, check you username and password'
            })
        
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))
    
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "massage": "logged out"
    })




def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    
    if request.method == "POST": 
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # to ensure username doesn't exsist
        if User.objects.filter(username=username).exists():
            return render(request, "users/register.html", {
                "message": "username is aready exist"
            })

        if password != confirm_password:
            return render(request, "users/register.html", {
                "message": "passowrd and confirm_password not match"
            })
        
        # to ensure that password doesn't exsist
        if User.objects.filter(password=password).exists():
            return render(request, "users/register.html", {
            "message": "password is aready exist"
            })

        
 


        regiser_errors = {
        "UNIQUE constraint failed: auth_user.username": 'username is already exist',
        }
        try:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        except Exception as error:
            error = str(error)
            if error not in regiser_errors:
                print(error)
                regiser_errors[error] = "An error occurred while creating your account. Please try again later."

            return render(request, "users/register.html", {
                "message": regiser_errors[error]
            })
        else:
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))


        
    if User.objects.filter(password='harm5alaa').exists():
        print("exist king ")
    else:
        print("doesn't")


    return render(request, "users/register.html")   
        
