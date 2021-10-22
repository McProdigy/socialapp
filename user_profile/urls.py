from django.urls import path
from .views import Profile
from social.views import PostTweet

urlpatterns = [
    path('<slug:profile_username>/', Profile.as_view(), name='profile'),
    path('<slug:profile_username>/post/', PostTweet.as_view(), name='post-tweet' )
]