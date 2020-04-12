from django.urls import path
from . import views

urlpatterns = [
    path('shopping', views.func_shopping, name='shopping')  
]