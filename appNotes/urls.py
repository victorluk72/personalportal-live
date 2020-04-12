from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.func_notes, name='notes')  
]