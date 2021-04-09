from django.shortcuts import render
from .models import Location, Place, City
from django.views import generic


def index(request):
    """View function for home page of site."""

    num_places = Place.objects.all().count()
    num_cities = City.objects.all().count()

    context = {
        'num_places': num_places,
        'num_cities': num_cities,
    }

    return render(request, 'index.html', context=context)


class CityListView(generic.ListView):
    model = City
    paginate_by = 10

