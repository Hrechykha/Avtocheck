from django.shortcuts import render, redirect
from .forms import AvtoForm, MyRegistrationForm
from .models import Avto
from django.contrib import messages


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def add_car(request):
    error = ''
    if request.method == 'POST':
        form = AvtoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные по авто успешно добавлены.')
        else:
            error = 'Форма не верно заполнена'

    form = AvtoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_car.html', context)


def search_car(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
    avto = AvtoForm.objects.filter(asset_desc__icontains=q)
    return render(request, 'main/view_car_filter.html', {'avto_data': avto})


def sign_up(request):
    error = ''
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно зарегистрирован.')
        else:
            error = 'Форма не верно заполнена'

    form = MyRegistrationForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/sign_up.html', context)


def contacts(request):
    return render(request, 'main/contacts.html')

def view_car(request):
    avto = Avto.objects.all()
    return render(request, 'main/view_car.html', {'avto_data': avto})