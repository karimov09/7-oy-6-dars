from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from .models import FoodType, Food, Like, Comment
from .forms import FoodForm, CommentForm, LoginForm, RegisterForm
from django.contrib import messages

def home_view(request):
    food_types = FoodType.objects.all()
    foods = Food.objects.all()
    return render(request, 'home.html', {'food_types': food_types, 'foods': foods})

@login_required
@permission_required('fastfood_app.add_food', raise_exception=True)
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodForm()
    return render(request, 'food_form.html', {'form': form})

@login_required
@permission_required('fastfood_app.change_food', raise_exception=True)
def update_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodForm(instance=food)
    return render(request, 'food_form.html', {'form': form})

@login_required
@permission_required('fastfood_app.delete_food', raise_exception=True)
def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        food.delete()
        return redirect('home')
    return render(request, 'food_confirm_delete.html', {'food': food})

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.korishlar_soni += 1
    food.save()
    return render(request, 'food_detail.html', {'food': food})

@login_required
def add_like(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    like, created = Like.objects.get_or_create(food=food, user=request.user)
    if not created:
        like.delete() 
    return redirect('home')

@login_required
def add_comment(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.food = food
            comment.user = request.user
            comment.save()
            return redirect('food_detail', pk=food.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'food': food})

@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return HttpResponseForbidden("You can only edit your own comments")
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('food_detail', pk=comment.food.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'fastfood_app/update_comment.html', {'form': form, 'food': comment.food})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return HttpResponseForbidden("You can only delete your own comments")
    food_id = comment.food.id
    comment.delete()
    return redirect('food_detail', pk=food_id)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Login yoki parol notogri!")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
