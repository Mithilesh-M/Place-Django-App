from django.contrib import admin
from .models import Place, Location, City
from django.contrib.gis.admin import OSMGeoAdmin

admin.site.register(Location)
admin.site.register(City)
admin.site.register(Place)