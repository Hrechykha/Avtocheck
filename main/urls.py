from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('view_car', views.view_car),
    path('add_car', views.add_car),
    path('sign_up', views.sign_up),
    path('contacts', views.contacts),
]
