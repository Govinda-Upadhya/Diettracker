from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
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
    return render(request,"diettracker/signup2.html",{
        'signupform':signupform,
    })

def signin(request):
    signinform=SignInForm()
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user=user)
            return redirect('tracker')
    return render(request,"diettracker/signin.html",{
        "signinform":signinform
    })

def delete(request):
    pass
def tracker(request):
    foods=Food.objects.all()
    if request.method=="POST":
        food=request.POST['food_consumed']
        consume = Food.objects.get(foodname=food)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
    consumed_food = Consume.objects.filter(user=request.user)
    protein=0
    carbs=0
    calories=0
    fats=0
    total=0
    for food in consumed_food:
        protein=round(food.food_consumed.protein+protein,2)
        fats=round(food.food_consumed.fats+fats,2)
        carbs=round(food.food_consumed.carbs+carbs,2)
        calories=round(food.food_consumed.calorie+calories,2)
    total=protein+fats+calories
    dailygoal=(protein+fats+carbs+calories)/2000*100
    fats_percentage=fats/total*100
    protein_percentage=protein/total*100
    calories_percentage=calories/total*100
    breakdown={
        "Fats":fats_percentage,
        "Protein":protein_percentage,
        "Calories":calories_percentage
    }
    return render(request,"diettracker/tracker.html",{
        "foods":foods,
        'consumed_food':consumed_food,
        'protein':protein,
        "carbs":carbs,
        "fats":fats,
        "calories":calories,
        "dailygoal":dailygoal,
        "breakdown":breakdown,
        "calories_percentage":calories_percentage,
        'fats_percentage':fats_percentage,
        'protein_percentage':protein_percentage
    })
def delete(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('tracker')
    return render(request,'diettracker/delete.html')