from django.contrib import admin
from .models import *
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display=('foodname','calorie')
class ConsumerAdmin(admin.ModelAdmin):
    list_display=('user','food')

admin.site.register(Food,FoodAdmin)
admin.site.register(Consume,ConsumerAdmin)
