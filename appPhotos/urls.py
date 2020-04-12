from django.urls import path
from . import views

urlpatterns = [
    path('photos', views.func_photos, name='photos')  
]