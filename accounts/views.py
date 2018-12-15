from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from accounts.forms import SigninForm, SignupForm
from tweet.forms import TweetForm

# Create your views here.

def frontpage(request):
    if request.user.is_authenticated:
        return redirect("/" + "profile.html" + "/")
    else:
        if request.method == "POST":
            if "signupform" in request.POST:
                signupform = SignupForm(data=request.POST) 
                signinform =  SigninForm()

                if signupform.is_valid():
                    username = signupform.cleaned_data["username"]
                    password = signupform.cleaned_data["password1"]
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect("/")
                else:
                    signinform = SigninForm(data=request.POST)
                    signupform = SigninForm()

                    if signinform.is_valid():
                        login(request, signinform.get_user())
                        return redirect("/")

            else:
                signupform = SigninForm()
                signinform = SigninForm()

            return render(request, "frontpage.html", {"signupform": signupform, "signinform": signinform})


def signout(request):
    logout(request)
    return redirect("/")


def profiles(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)

        if request.method == "POST":
            form = TweetForm(data=request.POST)
            if form.is_valid()
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()

            redirecturl = request.POST.get("redirect", "/")
            return redirect(redirecturl)
        else:
            form = TweetForm()
        return render(request, "profile.html", {"user": user, "form": form})
    else:
        return redirect("/")


def follows(request, username):
    user = User.objects.get(username=username)
    tweeterprofiles = user.tweeterprofile.follows
    return render(request, "users.html", {"title": "Follows", "tweeterprofiles": tweeterprofiles})


def followers(request, username):
    user = User.objects.get(username=username)
    tweeterprofiles = user.tweeterprofile.followed_by
    return render(request, "user.html", {"title": "Followers", "tweeterprofiles": tweeterprofiles})