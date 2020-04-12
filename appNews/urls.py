from django.urls import path
from . import views

urlpatterns = [
    path('news', views.func_news, name='news')  
]