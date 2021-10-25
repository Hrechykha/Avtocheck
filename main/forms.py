from .models import Avto
from django.forms import ModelForm, TextInput, Textarea, ImageField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AvtoForm(ModelForm):
    class Meta:
        model = Avto
        fields = ["manufacturer", "vin", "description", "date", "image"]
        labels = {"manufacturer": 'Введите текст', "vin": 'Выберите группу'}
        help_text = {'manufacturer': 'Любую абракадабру',
                     'vin': 'Из уже существующих'}
        widgets = {
            "manufacturer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ведите марку автомобиля'
            }),
            "vin": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ведите VIN номер автомобиля'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ведите описание'
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ведите дату осмотра автомобиля'
            }),
        }


class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label=('Имя пользователя:'),
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Введите имя пользователя"}),
        required=True,
        error_messages={'required': 'Please enter your name'}
    )

    email = forms.CharField(
        label=('Email адрес:'),
        max_length=15,
        widget=forms.EmailInput(attrs={"placeholder": "Введите электронную почту"}),
        required=True,
        error_messages={'required': 'Please enter your name'}
    )

    password1 = forms.CharField(
        label=('Пароль:'),
        max_length=15,
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"}),
        help_text='Пароль должен содержать минимум 8 символов. '
                  'Пароль не должен быть одним из широоко распространённых паролей.',
    )

    password2 = forms.CharField(
        label=('Повторите пароль:'),
        max_length=15,
        widget=forms.PasswordInput(attrs={"placeholder": "Введите подтверждение пароля"}),
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SearchAvto(ModelForm):
    vin_search = forms.CharField(
        label=('VIN номер:'),
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Введите VIN номер автомобиля"}),
        required=True,
        error_messages={'required': 'Введите VIN номер автомобиля'}
    )