from django.urls import path
from accounts.views import frontpage, signout, profile

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("signout/", signout, name="signout"),
    path("<str:username>/", profile, name="profile"),
]
