from django.urls import path
from . import views

urlpatterns = [
    path('stocks', views.func_stocks, name='stocks')  
]