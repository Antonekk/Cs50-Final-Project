import random
import string
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Option, Votes, Poll

# Create your views here.
def index (request):
    return render(request, "Pollapp/index.html")

@login_required(redirect_field_name='login')
def profile(request):
    return render(request, "Pollapp/profile.html")


def polls(request):
    all_public_polls = Poll.objects.filter(private=False)
    return render(request, "Pollapp/polls.html", {
        "polls":all_public_polls,
    })

def create_poll(request):
    if request.method == "GET":
        return render(request, "Pollapp/create_poll.html")
    elif request.method == "POST":
        question = request.POST['question_name']
        try:
            is_private = request.POST['private']
            is_private = True
        except:
            is_private = False
        answers = []
        for i in range(1,11):
            answer_num = 'answer'+str(i)+'_name'
            try : 
                answers.append(request.POST[answer_num])
            except:
                break
        url = ''.join(random.choice(string.ascii_letters) for i in range(20))
        if_url_exists = Poll.objects.filter(url=url)
        while len(if_url_exists) != 0:
            url = ''.join(random.choice(string.ascii_letters) for i in range(20))
            if_url_exists = Poll.objects.filter(url=url)

        poll = Poll(
            user = request.user,
            poll_question = question,
            private = is_private,
            url = url

        )
        poll.save()
        for answer in answers:
            try:
                option = Option.objects.get(question=answer)
            except:
                option = Option(
                    question = answer
                )
                option.save()
            poll.options.add(option)
        poll.save()
        return HttpResponseRedirect(reverse("polls"))



#Register, Login and Logout functions

def register (request):
    if request.method == "POST":
        # Gets both passwords value and checks if they match
        password = request.POST["password"]
        password_confirmation = request.POST["password_confirmation"]
        if password != password_confirmation:
            return render(request, "Pollapp/register.html", {
                "message": "Passwords must match"
            })

        #Gets both username and email from user input
        username = request.POST["username"]
        email = request.POST["email"]

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except:
            return render(request, "Pollapp/register.html", {
                "message": "Username or Email already taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("profile"))
    elif request.method == "GET":   
        return render(request, "Pollapp/register.html")

def login_page(request):
    if request.method == "POST":
        #Get user data
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        #check if this user exists
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("profile"))
        else:
            return render(request, "Pollapp/login.html", {
                "message": "Invalid username or/and password"
            })

    elif request.method == "GET":   
        return render(request, "Pollapp/login.html")

def logout_function(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))




