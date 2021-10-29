from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from .models import Avto
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class AvtoForm(ModelForm):
    class Meta:
        model = Avto
        fields = ["manufacturer", "vin", "description", "date", "image"]
        labels = {"manufacturer": 'Введите текст', "vin": 'Введите VIN'}
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
        }


class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label=('Имя пользователя:'),
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Введите имя пользователя"}),
        required=True,
        error_messages={'required': 'Please enter your name', 'min_length': 'very short entry',
                        'invalid': 'Improper format'},
    )

    email = forms.CharField(
        label=('Email адрес:'),
        max_length=30,
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


class SearchAvto(AvtoForm):
    vin_search = forms.CharField(
        label=('VIN номер:'),
        max_length=17,
        validators=[MinLengthValidator(17)],
        widget=forms.TextInput(attrs={"placeholder": "Введите VIN номер автомобиля"}),
        required=True,
        error_messages={'required': 'Введите VIN номер автомобиля'},
        help_text="Enter a date between now and 4 weeks (default 3)."
    )

    def clean_vin(self):
        cleaned_data = super(SearchAvto, self).clean()
        vin = cleaned_data.get(self, 'vin_search')
        # manufacturer = cleaned_data.get('manufacturer')
        if len(vin) < 17:
            raise ValidationError('VIN должен быть не менее 17 символов.')


class LoginUser(AuthenticationForm):
    username = forms.CharField(
        label=('Имя пользователя:'),
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Введите имя пользователя"}),
        required=True,
        error_messages={'required': 'Имя пользователя не может быть пустым.'}
    )
    password = forms.CharField(
        label=('Пароль:'),
        max_length=15,
        widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"}),
        required=True,
        error_messages={'required': 'Пароль не может быть пустым.'}
    )