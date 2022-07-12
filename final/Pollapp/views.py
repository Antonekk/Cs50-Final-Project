from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User

# Create your views here.
def index (request):
    return render(request, "Pollapp/index.html")

def register (request):
    if request.method == "POST":
        # Gets both passwords value and checks if they match
        password = request.POST["password"]
        password_confirmation = request.POST["password_confirmation"]
        if password != password_confirmation:
            return render(request, "Pollapp/register.html")

        #Gets both username and email from user input
        username = request.POST["username"]
        email = request.POST["email"]

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except:
            return render(request, "Pollapp/register.html")
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    elif request.method == "GET":   
        return render(request, "Pollapp/register.html")

def login_page (request):
    if request.method == "POST":
        #Get user data
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        #check if this user exists
        if user is not None:
            login(request, user)
        else:
            return render(request, "Pollapp/login.html")

    elif request.method == "GET":   
        return render(request, "Pollapp/login.html")


