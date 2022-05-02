from django.shortcuts import render, redirect
from .models import Station
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# # Add the following import
# from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

# Create your views here.

class StationCreate(LoginRequiredMixin, CreateView):
  model = Station
  fields = ['name', 'company', 'date', 'price', 'cards_accepted', 'zipcode']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')

    else:
      error_message = 'Invalid Sign Up - Please try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class StationDelete(LoginRequiredMixin, DeleteView):
  model = Station
  success_url = '/stations/'


class PriceUpdate(LoginRequiredMixin, UpdateView):
  model = Station
  fields = ["price"]

def stations_index(request):
  stations = Station.objects.all()
  return render(request, 'stations/index.html', {'stations': stations})
@login_required
def stations_detail(request, station_id):
  station = Station.objects.get(id=station_id)
  return render(request, 'stations/detail.html', {'station': station})

def about(request):
  return render(request, 'about.html')

