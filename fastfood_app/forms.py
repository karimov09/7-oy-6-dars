from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_type', 'nomi', 'tarkibi', 'narxi','rasm']
