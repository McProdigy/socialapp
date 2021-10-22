from django.shortcuts import render
from django.views.generic import View
from .forms import TweetForm
from .models import HashTag

# Create your views here.

class PostTweet(View):
    def post(self, request, profile_username, *args, **kwargs):
        tweet_form = TweetForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=profile_username)
            tweet = Tweet(text=form.cleaned_data['text'],
            country = form.cleaned_data['country'],
            user=user
            )
            tweet.save()

            words = form.cleaned_data['text'].split(' ')
            for word in words:
                if word[0] == '#':
                    hashTag, created = HashTag.objects.get_or_create(name=word[1:])
                    hashTag.tweet.add(tweet)

                return HttpResponseRedirect('/user/'+profile_username)

class HashTagCloud(View):
    def get(self, request, hashTag_name, *args, **kwargs):
        hashtag = HashTag.objects.get(name=hashTag_name)
        
        params['tweets'] = hastag.tweet

        return render(request, 'social/hashtag.html', params)