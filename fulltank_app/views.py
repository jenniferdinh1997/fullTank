from django.shortcuts import render
from .models import Stations

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')


# Create your views here.
def stations_index(request):
  return render(request, '', {'stations': stations})
