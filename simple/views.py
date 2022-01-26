from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Project , Tag
from .forms import ProjectForm, SignupForm

from django.contrib.auth.decorators import login_required

# Create your views here.

projectlist=[
    {
        "id" : "1" ,
        "title" : "Ecommerce Website" ,
        "description" : "Full functional Website"
    },  
    {
        "id" : "2" ,
        "title" : "Social Network" ,
        "description" : "Nice Work i am still working on"
    },
    {
        "id" : "3" ,
        "title" : "Port Website" ,
        "description" : "Portfolio functional Website"
    },
]

def open(request):
    my_dict = {
        "firstname" : "Temitope",
        "lastname" : "James",
        "nickname" : "Mufasa",
        "project" : projectlist

    }
    return render(request, "simple/open.html", context=my_dict)

def wow(request, fig):

    return HttpResponse("This is the response and this is the para: "+fig+" ")    

def paras(request, pk):
    projectobj = None
    for i in projectlist:
        if i['id'] == pk:
            projectobj = i
    dict = { "pk" : pk, "obj":projectobj}

    return render(request, "simple/paras.html", context = dict)
    
def database(request):
    project = Project.objects.all()
    return render(request, "simple/database.html", {"project":project,})

def single(request, num):
    projectobj = Project.objects.get(id=num)
    tags = projectobj.tag.all()

    mydict = { "tags" : tags, "num":num, "obj":projectobj}
    return render(request, "simple/single.html", context=mydict)

@login_required(login_url='user:loginform')
def register(request):
    registerForm = ProjectForm()

    if request.method == 'POST':
        # print(request.POST["title"])
        registerForm = ProjectForm(request.POST, request.FILES)
        if registerForm.is_valid():
            registerForm.save()      
            return redirect("simple:database")
    
    my_dict = {"register" : registerForm,}
    return render(request, "forms/register.html", context=my_dict)
@login_required(login_url='user:loginform')
def update(request, pk):
    projectid = Project.objects.get(id=pk)
    registerForm = ProjectForm(instance=projectid)

    if request.method == 'POST':
        # print(request.POST["title"])
        registerForm = ProjectForm(request.POST, request.FILES, instance=projectid)

        if registerForm.is_valid():
            registerForm.save()      
        return redirect("simple:database" )
    
    my_dict = {"register" : registerForm,}
    return render(request, "forms/edit.html", context=my_dict)

@login_required(login_url='user:loginform')
def delete(request, pk):
    project = Project.objects.get(id =pk)
    if request.method == "POST":
        project.delete()
        return redirect("simple:database")

    my_dict = {
        "object":project
    }
    return render(request, "forms/delete.html", my_dict)
    

    
