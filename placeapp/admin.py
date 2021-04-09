#from django.contrib import admin
from .models import Location, Place, City
from django.contrib.gis import admin
# Register your models here.
admin.site.register(Location)
admin.site.register(Place)
admin.site.register(City)