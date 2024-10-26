from django import forms
from .models import Food, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_type', 'nomi', 'tarkibi', 'narxi', 'rasm']
        labels = {
            'food_type': 'Oziq-ovqat turi',
            'nomi': 'Oziq-ovqat nomi',
            'tarkibi': 'Tarkibi',
            'narxi': 'Narxi',
            'rasm': 'Rasm',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Komment',
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

