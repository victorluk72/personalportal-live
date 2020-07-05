from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('samsebeskazal/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/api/rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('contacts/', include('appContacts.urls')),
    path('calendar/', include('appCalendar.urls')),
    path('news/', include('appNews.urls')),
    path('notes/', include('appNotes.urls')),
    path('photos/', include('appPhotos.urls')),
    path('shopping/', include('appShopping.urls')),
    path('stocks/', include('appStocks.urls')),
    path('weather/', include('appWeather.urls')),
]
