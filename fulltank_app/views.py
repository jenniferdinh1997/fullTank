from django.shortcuts import render
from .models import Station
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# # Add the following import
# from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

# Create your views here.
class StationCreate(CreateView):
  model = Station
  fields = ['name', 'company', 'date', 'price', 'cards_accepted', 'zipcode']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class StationDelete(DeleteView):
  model = Station
  success_url = '/stations/'

class PriceUpdate(UpdateView):
  model = Station
  fields = ["price"]

def stations_index(request):
  stations = Station.objects.all()
  return render(request, 'stations/index.html', {'stations': stations})

def stations_detail(request, station_id):
  station = Station.objects.get(id=station_id)
  return render(request, 'stations/detail.html', {'station': station})

def about(request):
  return render(request, 'about.html')

