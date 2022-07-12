from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, "Pollapp/index.html")

def register (request):
    if request.method == "POST":
        pass
    elif request.method == "GET":   
        return render(request, "Pollapp/register.html")

def login (request):
    if request.method == "POST":
        pass
    elif request.method == "GET":   
        return render(request, "Pollapp/login.html")
