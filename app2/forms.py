from django import forms

from .models import Category


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
        }
