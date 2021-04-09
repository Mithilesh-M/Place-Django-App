from django.shortcuts import render
from .models import Location, Place, City
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateCityForm, CreatePlaceForm


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

            return HttpResponseRedirect(reverse('cities') )

    else:
        form = CreateCityForm()

    context = {
        'form': form,
    }

    return render(request, 'placeapp/create_city.html', context)

def CreatePlace(request):
    """View function for Creating Place."""

    if request.method == 'POST':

        form = CreatePlaceForm(request.POST)

        if form.is_valid():
            place = Place(title=form.cleaned_data['title'],description=form.cleaned_data['description'],address=form.cleaned_data['address'],phone=form.cleaned_data['phone'],city=form.cleaned_data['city'],type_of_place=form.cleaned_data['type_of_place'],)
            place.save()

            return HttpResponseRedirect(reverse('places'))

    else:
        form = CreatePlaceForm()

    context = {
        'form': form,
    }

    return render(request, 'placeapp/create_place.html', context)

def PlaceDelete(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    place = get_object_or_404(Place, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        place.delete()
        return HttpResponseRedirect(reverse('places'))

    context = {
        'place': place,
    }

    return render(request, 'placeapp/delete_place.html', context)
