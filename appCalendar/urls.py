from django.urls import path
from . import views

urlpatterns = [
    path('calendar', views.func_calendar, name='calendar')  
]