from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodType, Food
from django.contrib.auth.decorators import login_required, permission_required
from .forms import FoodForm

def home_view(request):
    food_types = FoodType.objects.all()
    foods = Food.objects.all()
    return render(request, 'home.html', {'food_types': food_types, 'foods': foods})


def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodForm()
    return render(request, 'food_form.html', {'form': form})

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.korishlar_soni += 1
    food.save()
    return render(request, 'fastfood_app/food_detail.html', {'food': food})

@login_required
@permission_required('fastfood_app.add_food', raise_exception=True)
def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FoodForm()
    return render(request, 'fastfood_app/food_form.html', {'form': form})

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
    return render(request, 'fastfood_app/food_form.html', {'form': form})

@login_required
@permission_required('fastfood_app.delete_food', raise_exception=True)
def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        food.delete()
        return redirect('home')
    return render(request, 'fastfood_app/food_confirm_delete.html', {'food': food})
