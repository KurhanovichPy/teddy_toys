from django.contrib.auth.models import User
from django.forms import (ModelForm, Form, CharField, PasswordInput, ValidationError, TextInput)


class UserRegistrationForm(ModelForm):
    password = CharField(widget=PasswordInput(attrs={'class': 'forms', 'placeholder': 'Пароль'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'forms', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        widgets = {
            'username': TextInput(attrs={
                'class': 'forms',
                'placeholder': 'Логин'
            }),
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
            })
        }

    def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise ValidationError('Пароли не совпадают')
            return cd['password2']


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={'class': 'forms', 'placeholder': 'Логин'}))
    password = CharField(widget=PasswordInput(attrs={'class': 'forms', 'placeholder': 'Пароль'}))
