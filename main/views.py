from django.shortcuts import render, redirect
from .forms import AvtoForm, MyRegistrationForm
from .models import Avto
from django.contrib import messages
import time


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def add_car(request):
    error = ''
    if request.method == 'POST':
        form = AvtoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные по авто успешно добавлены.')
            return redirect('/success_adding_car')
        else:
            error = 'Форма не верно заполнена'

    form = AvtoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_car.html', context)


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


def search(request):
    avtos=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        avtos = Avto.objects.filter(vin__exact=search)
    return render(request, 'main/search_results.html', {
        'avtos': avtos,
    })


def success_adding_car(request):
    return render(request, 'main/success_adding_car.html')