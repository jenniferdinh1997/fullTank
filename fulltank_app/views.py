from django.shortcuts import render
from .models import Station
from django.views.generic.edit import CreateView, DeleteView

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

# Create your views here.
class StationCreate(CreateView):
  model = Station
  fields = '__all__'

class StationDelete(DeleteView):
  model = Station
  success_url = '/stations/'

def stations_index(request):
  stations = Station.objects.all()
  return render(request, 'stations/index.html', {'stations': stations})

def stations_detail(request):
  station = Station.objects.get(id=station_id)
  return render(request, 'stations/detail.html', {'station': station})

def about(request):
  return render(request, 'about.html')
