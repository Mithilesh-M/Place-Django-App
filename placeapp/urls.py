from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cities/', views.CityListView.as_view(), name='cities'),
    path('places/', views.PlaceListView.as_view(), name='places'),
]