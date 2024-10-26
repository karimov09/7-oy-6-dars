from django.contrib import admin
from .models import FoodType, Food, Like, Comment

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('nomi',)
    search_fields = ('nomi',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'food_type', 'narxi', 'korishlar_soni')
    list_filter = ('food_type',)
    search_fields = ('nomi', 'tarkibi')
    ordering = ('-korishlar_soni',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('food', 'user')
    list_filter = ('food',)
    search_fields = ('food__nomi', 'user__username')  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('food', 'user', 'content', 'created_at')
    list_filter = ('created_at', 'food')
    search_fields = ('content', 'user__username', 'food__nomi')
    ordering = ('-created_at',)  