from django.contrib import admin
from .models import Place, Location, City

admin.site.register(Location)
admin.site.register(City)
admin.site.register(Place)