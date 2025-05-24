from django import forms
from .models import Meal, MealIngredient
from django.forms import inlineformset_factory


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['type', 'name', 'description']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select select2'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название блюда'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание (необязательно)', 'rows': 3}),
        }


class MealIngredientForm(forms.ModelForm):
    class Meta:
        model = MealIngredient
        fields = ['product', 'quantity', 'unit']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select select2'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
        }

MealIngredientFormSet = inlineformset_factory(
    Meal,
    MealIngredient,
    form=MealIngredientForm,
    extra=1,
    can_delete=True,
)