from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stations/', views.stations_index, name='index'),
    path('stations/create/', views.StationCreate.as_view(), name='stations_create'),
]