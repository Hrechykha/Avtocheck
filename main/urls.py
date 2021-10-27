from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('view_car', views.view_car),
    path('add_car', views.add_car),
    path('sign_up', views.sign_up),
    path('contacts', views.contacts),
    path('search_results', views.search),
    path('success_adding_car', views.success_adding_car),
    path('success_sign_up', views.success_sign_up),
]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

