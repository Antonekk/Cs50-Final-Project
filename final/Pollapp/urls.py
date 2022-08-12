from django.urls import path

from . import views
urlpatterns = [
    path('', views.index , name="index"),
    path('contact', views.contact , name="contact"),
    path('about', views.about , name="about"),
    path('register', views.register , name="register"),
    path('login', views.login_page , name="login"),
    path('logout', views.logout_function, name="logout"),
    path("profile/<str:category>/<str:page_num>", views.profile , name="profile"),
    path("polls/<str:page_num>", views.polls, name="polls"),
    path("create_poll", views.create_poll, name="create_poll"),
    path("poll/<str:url>", views.poll_page, name="poll_page"),
    path("like/<str:url>", views.like, name="like"),
    path("deactivate/<str:url>", views.deactivate, name="deactivate"),
]
