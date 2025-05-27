from django.shortcuts import render, redirect, get_object_or_404
from .forms import MealForm
from .models import Meal
from django.http import JsonResponse

# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
# @login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.created_by = request.user
            meal.save()
            form.save_m2m()  
            return redirect('meal-list')
    else:
        form = MealForm()

    return render(request, 'meal.html', {'form': form})

# @login_required
def meal_list(request):
    meals = Meal.objects.all().order_by('-id')
    return render(request, 'meal_list.html', {'meals': meals})



def edit_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = MealForm(instance=meal)

    return render(request, 'meal_list.html', {'form': form, 'meal': meal})


# @csrf_exempt
# def delete_meal(request, pk):
#     if request.method == "POST":
#         meal = get_object_or_404(Meal, pk=pk)
#         meal.delete()
#         return JsonResponse({"status": "deleted"})
#     return JsonResponse({"error": "invalid request"}, status=400)