# forms.py
from django import forms
from .models import Meal, MealIngredient

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['type', 'name', 'description']  # removed 'products'


class MealIngredientForm(forms.ModelForm):
    class Meta:
        model = MealIngredient
        fields = ['product', 'quantity', ]
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

