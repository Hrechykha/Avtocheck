from .models import Avto
from django.forms import ModelForm, TextInput, Textarea

class AvtoForm(ModelForm):
    class Meta:
        model = Avto
        fields = ["manufacturer", "vin", "description", "date"]
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
            })
        }
