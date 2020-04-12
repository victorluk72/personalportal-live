from django.urls import path
from . import views

urlpatterns = [
    path('weather', views.func_weather, name='weather')  
]