from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
import requests
import json

# Create your views here.
#This function handles the signin functionality of the webapp
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
#This function handles the signin functionality of the webapp
def signin(request):
    signinform=SignInForm()
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user=user)
            return redirect('home')
    return render(request,"diettracker/signin.html",{
        "signinform":signinform
    })


def tracker(request):
    foods=Food.objects.all()
    goal=Goals.objects.filter(user=request.user)
    goals=goal[len(goal)-1]
    #api call to get the macronutrient of any food the user searches
    if request.method=="POST":
        food=request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        response = requests.get(api_url+food, headers={'X-Api-Key': 'jqhijkYNLf40YrpKTcq6Gw==WSgjDzVr8XG3thvT'})
        api=json.loads(response.content)
        data=api[0]
        foodtaken=Food(foodname=data['name'],
                        carbs=data['carbohydrates_total_g'],
                        fats=data['fat_total_g'],
                        calorie=data['calories'],
                        protein=data['protein_g'])
        
        exist=False
        for i in foods:
            if foodtaken.foodname==i.foodname:
                exist=True
                break
        if exist==False:
            foodtaken.save()
        consume = Food.objects.get(foodname=food)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
    consumed_food = Consume.objects.filter(user=request.user)
    protein=0
    carbs=0
    calories=0
    fats=0
    for food in consumed_food:
        protein=round(food.food_consumed.protein+protein,2)
        fats=round(food.food_consumed.fats+fats,2)
        carbs=round(food.food_consumed.carbs+carbs,2)
        calories=round(food.food_consumed.calorie+calories,2)
    fats_percentage=fats/goals.fats_goal*100
    protein_percentage=protein/goals.protein_goal*100
    calories_percentage=calories/goals.calorie_goal*100
    carbs_percentage=carbs/goals.carbohydrate_goal*100
    return render(request,"diettracker/tracker.html",{
        "foods":foods,
        "goals":goals,
        'consumed_food':consumed_food,
        'protein':protein,
        "carbs":carbs,
        "fats":fats,
        "calories":calories,
        "calories_percentage":calories_percentage,
        'fats_percentage':fats_percentage,
        'protein_percentage':protein_percentage,
        'carbs_percentage':carbs_percentage
    })
#this function handles all the personal daily goals of the users
def home(request):
    goalform=DailyGoalForm()

    if request.method=="POST":
        goalform=DailyGoalForm(request.POST)
        if goalform.is_valid():
            calorie_goal=goalform.cleaned_data['calorie_goal']
            protein_goal=goalform.cleaned_data['protein_goal']
            fats_goal=goalform.cleaned_data['fats_goal']
            carbohydrate_goal=goalform.cleaned_data['carbohydrate_goal']
            goals=Goals(user=request.user,calorie_goal=calorie_goal,protein_goal=protein_goal,fats_goal=fats_goal,carbohydrate_goal=carbohydrate_goal)
            goals.save()
    return render(request,"diettracker/home.html",{
        "dailygoals":goalform
    })
# the following two function is responsible for deleting one or all the food items respectively
def delete(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('tracker')
    return render(request,'diettracker/delete.html')
def deleteall(request):
    consumed_food = Consume.objects.filter(user=request.user)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('tracker')
    return render(request,'diettracker/deleteall.html')
