from django import forms
from django.forms import TextInput

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'Фамилия'
            }),
            'email': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'email'
            }),
            'address': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'Адрес'
            }),
            'postal_code': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'Индекс'
            }),
            'city': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'Город'
            })
        }
