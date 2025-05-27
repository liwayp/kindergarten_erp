from django import forms
from django.forms import inlineformset_factory
from .models import Meal, MealIngredient


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['type', 'name', 'description', 'products']
        labels = {
            'type': 'Тип приёма пищи',
            'name': 'Название блюда',
            'description': 'Описание',
            'products': 'Ингредиенты',
        }
        widgets = {
            'type': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название блюда'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'products': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
        }

class MealIngredientForm(forms.ModelForm):
    class Meta:
        model = MealIngredient
        fields = ['product', 'quantity', 'unit']
        labels = {
            'product': 'Продукт',
            'quantity': 'Количество',
            'unit': 'Единица измерения',
        }
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select select2'}),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00'
            }),
            'unit': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'грамм, мл и т.д.'
            }),
        }


MealIngredientFormSet = inlineformset_factory(
    Meal,
    MealIngredient,
    form=MealIngredientForm,
    extra=1,
    can_delete=True,
)


