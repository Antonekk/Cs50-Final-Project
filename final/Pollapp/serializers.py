from dataclasses import field
from rest_framework import serializers
from .models import  Option, Votes, Poll

class PollSerializer(serializers.ModelSerializer):
    class Meta():
        model = Poll
        fields = "__all__"
