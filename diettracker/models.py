from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#this model is store the macro-nutrient for the food searched by the user
class Food(models.Model):
   foodname=models.CharField(max_length=40)
   carbs=models.FloatField()
   protein=models.FloatField()
   fats=models.FloatField()
   calorie=models.FloatField()

   def __str__(self) -> str:
      return f"{self.foodname} {self.calorie}"
   
#this model is to store the food against the user.
class Consume(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   food_consumed=models.ForeignKey(Food,on_delete=models.CASCADE)

#this form is to store the personal daily goals for each user
class Goals(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   calorie_goal=models.FloatField()
   protein_goal=models.FloatField()
   fats_goal=models.FloatField()
   carbohydrate_goal=models.FloatField()