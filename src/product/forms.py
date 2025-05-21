from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'unit', 'minimum_threshold']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название продукта'}),
            'unit': forms.Select(choices=[
                ('кг', 'Килограммы'),
                ('л', 'Литры'),
                ('шт', 'Штуки'),
            ]),
            'minimum_threshold': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Минимум'}),
        }