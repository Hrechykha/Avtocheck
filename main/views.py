from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import AvtoForm, MyRegistrationForm, LoginUser
from .models import Avto
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
            #messages.success(request, 'Данные по авто успешно добавлены.')
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
            #messages.success(request, 'Пользователь успешно зарегистрирован.')
            return redirect('/success_sign_up')
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
    avto = Avto.objects.all().order_by('-date')

    return render(request, 'main/view_car.html', {'avto_data': avto})


def display_username(request):
    if request.user.is_authenticated():
        username = User.username
        return username


def search(request):
    avtos = None
    if request.GET.get('search'):
        search = request.GET.get('search')
        avtos = Avto.objects.filter(vin__exact=search)
    return render(request, 'main/search_results.html', {'avtos': avtos})


def success_adding_car(request):
    return render(request, 'main/success_adding_car.html')


def success_sign_up(request):
    return render(request, 'main/success_sign_up.html')


def login_request(request):
    form = LoginUser()
    if request.method == "POST":
        form = LoginUser(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Имя пользователя или пароль неверные.")
        else:
            messages.error(request, "Имя пользователя или пароль неверные.")
    context = {"login_form": form}
    return render(request, 'main/login.html', context)


def logout_request(request):
    logout(request)
    #messages.info(request, "You have successfully logged out.")
    return redirect('/')
