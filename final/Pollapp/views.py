from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, "Pollapp/index.html")

def register (request):
    return render(request, "Pollapp/register.html")

def login (request):
    return render(request, "Pollapp/login.html")
