from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    signupform=SignUpForm()
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        reenter=request.POST['reenter']

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect("signin")
    return render(request,"diettracker/signup.html",{
        'signupform':signupform,
    })

def signin(request):
    return HttpResponse("hello user")

def delete(request):
    pass
def tracker(request):
    pass
