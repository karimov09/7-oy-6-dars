from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class FoodType(models.Model):
    nomi = models.CharField(max_length=100, verbose_name="Tur nomi")

    class Meta:
        verbose_name = "Oziq-ovqat turi"
        verbose_name_plural = "Oziq-ovqat turlari"

    def __str__(self):
        return self.nomi

class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, verbose_name="Oziq-ovqat turi")
    nomi = models.CharField(max_length=100, verbose_name="Oziq-ovqat nomi")
    tarkibi = models.TextField(verbose_name="Tarkibi")
    narxi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    korishlar_soni = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")
    rasm = models.ImageField(upload_to='food_images/', blank=True, null=True, verbose_name="Rasm")

    class Meta:
        verbose_name = "Oziq-ovqat"
        verbose_name_plural = "Oziq-ovqatlar"

    def __str__(self):
        return self.nomi

class Like(models.Model):
    food = models.ForeignKey(Food, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('food', 'user') 
        verbose_name = "Like"
        verbose_name_plural = "Likes"

class Comment(models.Model):
    food = models.ForeignKey(Food, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Komment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Komment"
        verbose_name_plural = "Kommentlar"

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
