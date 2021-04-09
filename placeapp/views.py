from django.shortcuts import render
from .models import Location, Place, City
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateCityForm


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


class PlaceListView(generic.ListView):
    model = Place
    paginate_by = 10


class CityDetailView(generic.DetailView):
    model = City
    paginate_by = 10


class PlaceDetailView(generic.DetailView):
    model = Place
    paginate_by = 10


def CreateCity(request):
    """View function for Creating city."""

    if request.method == 'POST':

        form = CreateCityForm(request.POST)

        if form.is_valid():
            city = City(name=form.cleaned_data['name'])
            city.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('cities') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = CreateCityForm()

    context = {
        'form': form,
    }

    return render(request, 'placeapp/create_city.html', context)

