from django.shortcuts import render
from django.views.generic import View
from social.forms import TweetForm
from django.contrib.auth.models import User
from social.models import Tweet
# Create your views here.

class Profile(View):
    def get(self, request, profile_username, *args, **kwargs):
        user = User.objects.get(username=profile_username)
        tweets = Tweet.objects.filter(user=user)
        tweet_form = TweetForm()
        context = {
            'user':user,
            'tweets':tweets,
            'tweet_form':tweet_form
        }

        return render(request, 'profile.html', context)


