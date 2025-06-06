from django import forms
from .models import Children, ChildGroup

class ChildForm(forms.ModelForm):
    parent_email = forms.EmailField(label='Email родителя')

    class Meta:
        model = Children
        fields = ['name', 'age', 'group', 'parent_email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'parent_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = ChildGroup
        fields = ['name']