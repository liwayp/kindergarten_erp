from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import MealForm, MealIngredientFormSet
from .models import Meal
# from django.contrib.auth.decorators import login_required

# @login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        formset = MealIngredientFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            meal = form.save(commit=False)
            meal.created_by = request.user
            meal.save()

            formset.instance = meal
            formset.save()
            return redirect('meal-list')
    else:
        form = MealForm()
        formset = MealIngredientFormSet()

    return render(request, 'meal.html', {'form': form, 'formset': formset})

# @login_required
def meal_list(request):
    meals = Meal.objects.all().order_by('-id')
    return render(request, 'meal_list.html', {'meals': meals})
