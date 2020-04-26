from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appWeather.models import Location
import datetime


# View function for weather.html page
@login_required(login_url='login')
def func_weather(request):
    import requests  # pip install requests
    import json
     
    # city_db = list(Location.objects.values_list('city', flat=True))
    # countryCode_db = list(Location.objects.values_list('countryCode',flat=True))
    # concat_func = lambda x,y: x + "," + y
    # places_db = list(map(concat_func,city_db,countryCode_db))
    lats = list(Location.objects.filter(visible =True).order_by('seq').values_list('lat', flat=True))
    lons = list(Location.objects.filter(visible =True).order_by('seq').values_list('lon', flat=True))
    geoloc = list(Location.objects.filter(visible =True).order_by('seq').values_list('city', flat=True))
    #places_db = list(Location.objects.values_list('city', flat=True))
    print(geoloc)

    l_of_w = []
    cur_date = datetime.datetime.now()

    for lat, lon in zip(lats, lons):

        # api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + str(
        #     place) + "&units=metric&APPID=eabd78f72f8a61f5a4bc9c8707462840")
        api_request = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&units=metric&APPID=eabd78f72f8a61f5a4bc9c8707462840")
        #api_request = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=41.14&lon=-8.6&units=metric&APPID=eabd78f72f8a61f5a4bc9c8707462840")
        try:
            api_w = json.loads(api_request.content)
            current_temp = api_w['current']['temp']
           
            if current_temp < 0:
                temp_color = "style=\"color: #1065a9;\""
            else:
                temp_color = "style=\"color: #e99a1b;\""

            l_of_w.append(api_w)

        except:
            l_of_w = "Error"

    args = {'l_of_w': l_of_w, 
            'cur_date':cur_date,
            'geoloc':geoloc,
            'temp_color': temp_color
            }

    return render(request, 'weather/weather.html', args)
