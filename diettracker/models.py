from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Food(models.Model):
   foodname=models.CharField(max_length=40)
   carbs=models.FloatField()
   protein=models.FloatField()
   fats=models.FloatField()
   calorie=models.FloatField()

   def __str__(self) -> str:
      return f"{self.foodname} {self.calorie}"
class Consume(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   food=models.ForeignKey(Food,on_delete=models.CASCADE)
