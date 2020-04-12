from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# View function for weather.html page
@login_required(login_url='login')
def func_weather(request):

    return render(request, 'weather/weather.html', {})