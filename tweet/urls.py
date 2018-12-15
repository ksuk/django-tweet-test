from django.urls import path
from accounts.views import frontpage, signout, profile, following, follows, followers, follow, stopfollow
from tweet.views import feed

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("signout/", signout, name="signout"),
    path("<str:username>/", profile, name="profile"),
    path("feed/", feed, name="feed"),
    path("<str:username>/follows/", follows, name="follows"),
    path("<str:username>/following/", following, name="following"),
    path("<str:username>/follow/", follow, name="follow"),
    path("<str:username>/stopfollow/", stopfollow, name="stopfollow"),

]
