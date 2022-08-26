from asyncore import poll
import random
import string
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, Option, Votes, Poll
from .serializers import PollSerializer

# Create your views here.
def index (request):
    return render(request, "Pollapp/index.html")

def contact(request):
    return render(request, "Pollapp/contact.html")

def about(request):
    return render(request, "Pollapp/about.html")

def pagination(pag_objects, page_num):
    page_view = Paginator(pag_objects,5)
    page_info = {
        "contents": page_view.page(page_num).object_list,
        "number_of_pages": page_view.num_pages,
        "has_next": page_view.page(page_num).has_next(),
        "has_previous": page_view.page(page_num).has_previous(),
    }
    return page_info


@login_required(redirect_field_name='login')
def profile(request, category, page_num):
    if category == 'archived':
        user_polls = Poll.objects.filter(user=request.user, active=False).order_by("-id")
    elif category == 'liked':
        user_polls = Poll.objects.filter(active=True).order_by("-id")
        liked = []
        for u_poll in user_polls:
            if request.user in u_poll.likes.all():
                liked.append(u_poll)
        user_polls=liked
    elif category=='active':
        user_polls = Poll.objects.filter(user=request.user, active=True).order_by("-id")
    else:
        return render(request, "Pollapp/error_page.html" , {
            "message" : "Wrong url",
        })
    try:
        user_polls_info = pagination(user_polls, int(page_num))
    except:
         return render(request, "Pollapp/error_page.html" , {
            "message" : "Wrong url",
        })
    if int(page_num) >= 3:
        has_first = True
    else:
        has_first = False
    if int(page_num) <= user_polls_info["number_of_pages"]-2:
        has_last = True
    else:
        has_last = False
    return render(request, "Pollapp/profile.html", {
        "current_page_number": int(page_num),
        "polls" : user_polls_info["contents"],
        "number_of_pages": user_polls_info["number_of_pages"],
        "has_next": user_polls_info["has_next"],
        "next":int(page_num)+1,
        "has_previous": user_polls_info["has_previous"],
        "previous":int(page_num)-1,
        "has_first":has_first,
        "has_last": has_last,
        "category": category,
    })


def polls(request, page_num):
    all_public_polls = Poll.objects.filter(private=False, active=True).order_by("-id")

    try:
        user_polls_info = pagination(all_public_polls, int(page_num))
    except:
         return render(request, "Pollapp/error_page.html" , {
            "message" : "Wrong url",
        })
    if int(page_num) >= 3:
        has_first = True
    else:
        has_first = False
    if int(page_num) <= user_polls_info["number_of_pages"]-2:
        has_last = True
    else:
        has_last = False

    return render(request, "Pollapp/polls.html", {
        "current_page_number": int(page_num),
        "polls" : user_polls_info["contents"],
        "number_of_pages": user_polls_info["number_of_pages"],
        "has_next": user_polls_info["has_next"],
        "next":int(page_num)+1,
        "has_previous": user_polls_info["has_previous"],
        "previous":int(page_num)-1,
        "has_first":has_first,
        "has_last": has_last,
    })

def poll_page(request, url):
    try:
        poll_data = Poll.objects.get(url=url)
    except:
        return render(request, "Pollapp/error_page.html" , {
            "message" : "Wrong url",
        })
    if request.method == "GET":    
        all_votes = poll_data.votes.all()
        voted_option = ""
        for i in all_votes:
            if request.user == i.voter:
                voted_option = i.option
        
        options = poll_data.options.all()
        option_position = []
        votes_number = []
        for opt in options:
            votes_number.append(len(poll_data.votes.filter(option=opt)))
            option_position.append(opt.question)
        if request.user in poll_data.likes.all():
            liked = True
        else:
            liked = False
        return render(request, "Pollapp/poll_page.html" , {
                "poll" : poll_data,
                "options": poll_data.options.all(),
                "voted_on": voted_option,
                "options_set": option_position,
                "votes_number": votes_number,
                "liked": liked
            })
    elif request.method == "POST":
        vote = request.POST["option"]
        try:
            option = Option.objects.get(question=vote)
        except:
            return render(request, "Pollapp/error_page.html" , {
            "message" : "Wrong option",
        })
        all_votes = poll_data.votes.all()
        found = False
        for i in all_votes:
            if request.user == i.voter:
                if len(Votes.objects.filter(voter=request.user, option=option))==0:
                    vote = Votes.objects.create(voter=request.user, option=option)
                    vote.save()
                    poll_data.votes.add(vote)
                    i.delete()
                else:
                    i.delete()
                found=True
        if not found:
            vote = Votes.objects.create(voter=request.user, option=option)
            vote.save()
            poll_data.votes.add(vote)
        poll_data.save()

        return redirect("poll_page", url=url)


@login_required(redirect_field_name='login')
def deactivate(request, url):
    if request.method == 'POST':
        try:
            poll_data = Poll.objects.get(url=url)
            if request.user == poll_data.user:
                if poll_data.active == True:
                    poll_data.active = False
                else:
                    poll_data.active = True
                poll_data.save()
                return redirect("poll_page", url=url)
            else:
                return render(request, "Pollapp/error_page.html" , {
                "message" : "You are not the creator of this poll",
            })
        except:
            return render(request, "Pollapp/error_page.html" , {
                "message" : "Wrong url",
            })


@login_required(redirect_field_name='login')
def like(request, url):
    if request.method == 'POST':
        try:
            poll_data = Poll.objects.get(url=url)
            if request.POST["like"] == 'like':
                poll_data.likes.add(request.user)
                poll_data.save()
            elif request.POST["like"] == 'unlike':
                poll_data.likes.remove(request.user)
                poll_data.save()
            return redirect("poll_page", url=url)
        except:
            return render(request, "Pollapp/error_page.html" , {
                "message" : "Wrong url",
            })
    else:
        return render(request, "Pollapp/error_page.html" , {
                "message" : "Wrong method",
            })

@login_required(redirect_field_name='login')
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
            if answer == "":
                poll.delete()
                return render(request, "Pollapp/error_page.html", {
                "message": "Answer can't be empty"
                })
            if answers.count(answer) > 1:
                poll.delete()
                return render(request, "Pollapp/error_page.html", {
                "message": "There can't be two same answers"
                })
            try:
                option = Option.objects.get(question=answer)
            except:
                option = Option(
                    question = answer
                )
                option.save()
            poll.options.add(option)
        poll.save()
        return redirect("polls", page_num="1")



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
        return redirect("profile", category="active", page_num="1")
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
            return redirect("profile", category="active" , page_num="1")
        else:
            return render(request, "Pollapp/login.html", {
                "message": "Invalid username or/and password"
            })

    elif request.method == "GET":   
        return render(request, "Pollapp/login.html")

def logout_function(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@api_view(['GET'])
def api(request, api_data):
    if api_data == "all":
        api_all = Poll.objects.filter(private=False, active=True)
        serializer = PollSerializer(api_all, many=True)
        return Response(serializer.data)
    else:
        api_urls = Poll.objects.all().values_list('url', flat=True)
        if api_data in api_urls:
            try:
                api_data = Poll.objects.get(url=api_data)
                serializer = PollSerializer(api_data)
                return Response(serializer.data)
            except:
                return render(request, "Pollapp/error_page.html", {
                "message": "Error while geting data"
            })




