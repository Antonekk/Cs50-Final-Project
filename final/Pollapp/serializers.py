from dataclasses import field
from rest_framework import serializers
from .models import  User, Option, Votes, Poll


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = "username",

class OptionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Option
        fields = "question",

class VotesSerializer(serializers.ModelSerializer):
    option = OptionSerializer(read_only=True)
    class Meta():
        model = Votes
        fields = "option",

class PollSerializer(serializers.ModelSerializer):
    votes = VotesSerializer(read_only=True, many=True)
    likes = UserSerializer(read_only=True, many=True)
    options = OptionSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)
    likes = serializers.IntegerField(
        source='likes.count', 
        read_only=True
    )
    
    class Meta():
        model = Poll
        fields = "__all__"
