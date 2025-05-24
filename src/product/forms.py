from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'unit', 'minimum_threshold']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название продукта'}),
            'unit': forms.Select(choices=[
                ('kg', 'kilogramm'),
                ('l', 'litr'),
                ('pc', 'piece'),
            ]),
            'minimum_threshold': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Минимум'}),
        }