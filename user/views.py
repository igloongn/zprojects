from django.http.response import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as m 

# from django.contrib.messages import constants as messages

from .models import Profile, Skill 
from .forms import ProfileForm

@login_required(login_url='user:loginform')
def profile(request):
    profile = Profile.objects.all()
    # skills = Skill.objects.all()
    my_dict = {
        "profile" : profile,
        # "skills" : skills,
    }

    return render(request, "user/profile.html", my_dict)
    
def profileform(request):
    profile = ProfileForm
    my_dict = {
        "profile" : profile
    }

    return render(request, "user/profileform.html", my_dict)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topskill = profile.skill_set.exclude(description__exact='')
    otherskill = profile.skill_set.filter(description='')
    print(profile.name)

    my_dict = {
        "profile":profile,
        "topskills":topskill,
        "profile":otherskill,
    }
    return render(request, "user/userprofile.html", my_dict)


def logoutUser(request):
    logout(request)
    m.error(request, 'User has successfully logged out')
    return redirect('user:loginform')

 
def myprofile(request):


    keys = {

    }
    return render(request, 'user/myprofile.html', keys)
    
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('user:myprofile')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        # try:
        #   user = User.objects.get(username = username)
        #   print('Username Exist!,Username is a GOOO')
        # except:
        #   m.error(request, 'Username Does Not Exist!')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('Username Or Password Is a GOOO!!!')
            return redirect('user:myprofile')
        else:
            m.error(request, 'Username Or Password Is incorrect')
    keys = {
    }
    return render(request, 'user/login.html', keys)
   

def signupUser(request):
    # if request.user.is_authenticated:
    #     return redirect('user:myprofile')

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # print(request.POST['username'])
        # print(request.POST['password1'])
        # print(request.POST['password2'])

        if form.is_valid():
            form = form.save(commit=False)
            form.username=form.username.lower()
            form.save()
            m.success(request, "Registration Successful")
            return redirect('user:myprofile')


    keys = {
        'signup' : form
    } 
    return render(request, 'user/signup.html', keys)
    
    


    
    
    
       