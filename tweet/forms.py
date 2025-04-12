from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetFrom(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        # here used tuple because built in forms
        fields = ('username','email','password1','password2')

