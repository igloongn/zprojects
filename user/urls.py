from django.urls import path, re_path
from .views import logoutUser, myprofile, profile, profileform, signupUser, userProfile, loginUser
app_name = "user"

urlpatterns = [
    path("profilelist/", profile, name = "profile"),

    path("profileform/", profileform, name = "profileform"),

    path("myprofile/", myprofile, name = "myprofile"),

    path("loginform/", loginUser, name = "loginform"),
    path("logout/", logoutUser, name = "logout"),

    path("userprofile/<uuid:pk>/", userProfile, name = "userprofile"),

    path('signup/', signupUser, name='signup')
    
]

