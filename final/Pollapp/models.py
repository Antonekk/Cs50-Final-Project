from re import T
from tkinter import CASCADE
from tkinter.messagebox import QUESTION
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.



class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

class Option(models.Model):
    question = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.question}"
    
class Votes(models.Model):
    voter = models.ForeignKey(User,on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.voter}, voted on {self.option}"

class Poll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=24)
    poll_question = models.CharField(max_length=64)
    options = models.ManyToManyField(Option, symmetrical=False, blank=True , related_name="options")
    votes = models.ManyToManyField(Votes, symmetrical=False, blank=True, related_name="votes")
    likes = models.ManyToManyField(User, symmetrical=False, blank=True, related_name="likes")
    private = models.BooleanField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.poll_question}"



