from django.contrib import admin

# Register your models here.
from waypoints.models import WayPoint


@admin.register(WayPoint)
class WayPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'cityChineseName', 'cityEnglishName', 'airportChineseName', 'airportEnglishName',
                    'airportCode', 'countryCode', 'icao', 'iata', 'status', 'startTime', 'flightLevel',
                    'latitude', 'longitude', 'timeZone')
    list_per_page = 20