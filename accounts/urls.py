from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.func_logout, name='logout'),
    path('profile', views.func_profile, name='profile'),
]
