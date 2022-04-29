from django.shortcuts import render
from .models import Station
from django.views.generic.edit import CreateView

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

# Create your views here.
class StationCreate(CreateView):
  model = Station
  fields = '__all__'

def stations_index(request):
  stations = Station.objects.all()
  return render(request, 'stations/index.html', {'stations': stations})

