from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal, MealIngredient, MealPortion, MealPortionIngredient, WeeklyMenu
from .forms import MealForm, MealIngredientForm
from django.forms import inlineformset_factory
from django.contrib import messages
from product.models import Products
from django.contrib.auth.decorators import login_required

MealIngredientFormSet = inlineformset_factory(
    Meal, MealIngredient,
    form=MealIngredientForm,
    extra=1,  

    can_delete=True
)

@login_required(login_url='login')
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        formset = MealIngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            meal = form.save(commit=False)
            # meal.created_by = request.user
            meal.save()
            formset.instance = meal
            formset.save()
            return redirect('meal-list')
    else:
        form = MealForm()
        formset = MealIngredientFormSet()

    return render(request, 'meal_add.html', {'form': form, 'formset': formset})


@login_required(login_url='login')
def meal_list(request):
    meals = Meal.objects.all().order_by('-id')
    return render(request, 'meal_list.html', {'meals': meals})


@login_required
def edit_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    form = MealForm(request.POST or None, instance=meal)
    formset = MealIngredientFormSet(request.POST or None, instance=meal)

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('meal-list')

    return render(request, 'edit_meal.html', {
        'form': form,
        'formset': formset
    })

@login_required(login_url='login')
def meal_delete(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    meal.delete()
    return redirect('meal-list')



@login_required(login_url='login')
def count_portion_view(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    ingredients = MealIngredient.objects.filter(meal=meal)

    if request.method == 'POST':
        try:
            portion_count = int(request.POST.get('portion_count'))
            if portion_count <= 0:
                raise ValueError("Количество порций должно быть положительным числом.")
        except (ValueError, TypeError):
            messages.error(request, "Введите корректное количество порций.")
            return redirect('count-portion', meal_id=meal.id)

        for ing in ingredients:
            required_qty = ing.quantity * portion_count
            if ing.product.minimum_threshold < required_qty:
                messages.error(request, f"Недостаточно продукта: {ing.product.name}")
                return redirect('count-portion', meal_id=meal.id)

        log = MealPortion.objects.create(
            user=request.user,
            meal=meal,
            portion_count=portion_count
        )

        for ing in ingredients:
            product = ing.product
            total_required = ing.quantity * portion_count

            product.minimum_threshold -= total_required
            product.save()

            MealPortionIngredient.objects.create(
                log=log,
                product=product,
                quantity_used=total_required,
                unit=ing.unit or product.unit
            )

        messages.success(request, "Порции успешно рассчитаны и продукты обновлены.")
        return redirect('portion-list') 

    return render(request, 'count_portion.html', {
        'meal': meal,
        'ingredients': ingredients,
    })


@login_required(login_url='login')
def portion_log_list(request):
    logs = MealPortion.objects.select_related('meal', 'user').prefetch_related('ingredients', 'ingredients__product').order_by('-created_at')
    return render(request, 'portion_list.html', {'logs': logs})



@login_required(login_url='login')
def product_notification(request):
    products = Products.objects.all()

    product_data = []
    for product in products:
        quantity = product.minimum_threshold or 0
        if quantity < 50:
            status = 'Мало'
            color = 'red'
            status_sort = 0
        elif 50 <= quantity <= 150:
            status = 'Норма'
            color = 'orange'
            status_sort = 1
        else:
            status = 'Много'
            color = 'green'
            status_sort = 2

        product_data.append({
            'name': product.name,
            'unit': product.unit,
            'quantity': quantity,
            'status': status,
            'color': color,
            'sort': status_sort
        })
    sorted_pr = sorted(product_data, key=lambda x: x['sort'] )

    return render(request, 'notification.html', {'products': product_data})


@login_required(login_url='login')
def weekly_menu(request):
    if request.user.role != 'parents':
        return redirect('login')

    days_order = ['mon', 'tue', 'wed', 'thu', 'fri']
    menus = WeeklyMenu.objects.all().order_by('day')
    
    context = {
        'weekly_menus': {menu.day: menu.meals.all() for menu in menus if menu.day in days_order},
    }
    return render(request, 'weekly_menu.html', context)
