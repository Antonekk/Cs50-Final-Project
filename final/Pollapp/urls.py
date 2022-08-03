from django.urls import path

from . import views
urlpatterns = [
    path('', views.index , name="index"),
    path('register', views.register , name="register"),
    path('login', views.login_page , name="login"),
    path('logout', views.logout_function, name="logout"),
    path("profile", views.profile , name="profile"),
    path("polls", views.polls, name="polls"),
    path("create_poll", views.create_poll, name="create_poll"),
    path("polls/<str:url>", views.poll_page, name="poll_page"),
]
