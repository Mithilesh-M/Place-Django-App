from django.shortcuts import render
from .models import Location, Place, City

def index(request):
    """View function for home page of site."""

    num_places = Place.objects.all().count()
    num_cities = City.objects.all().count()

    context = {
        'num_places': num_places,
        'num_cities': num_cities,
    }

    return render(request, 'index.html', context=context)
