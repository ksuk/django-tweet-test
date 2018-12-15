from django.shortcuts import render
from .models import Tweet

# Create your views here.

def feed(request):
    userid = []
    for id in request.user.tweeterprofile.follows.all():
        userids.append(id)
    userids.append(request.user.id)
    tweets = Tweet.objects.filter(user_id__in=userids)[0:25]

    return render(request, "feed.html", {"twees": tweets})