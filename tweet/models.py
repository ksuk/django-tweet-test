from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, related_name="tweet", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

from django.db import models
from django.contrib.auth.models import User

class TweetProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False)

User.tweetprofile = property(lambda u:TweetProfile.objects.get_or_create(user=u)[0])    