from django.contrib import admin
from .models import FoodType, Food

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('nomi',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'food_type', 'narxi', 'korishlar_soni')
