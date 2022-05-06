from django.shortcuts import render, redirect
from .models import Station, Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

import boto3
import uuid

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'fulltank42'


# # Add the following import
# from django.http import HttpResponse
STATES = (
	('AL', 'ALABAMA'),
	('AK', 'ALASKA'),
  ('AS', 'AMERICAN SAMOA'),
	('AZ', 'ARIZONA'),
	('CA', 'CALIFORNIA'),
	('CZ', 'CANAL ZONE'),
	('CO', 'COLORADO'),
	('CT', 'CONNECTICUT'),
	('DE', 'DELAWARE'),
	('DC', 'DISTRICT OF COLUMBIA'),
	('FA', 'FLORIDA'),
	('GA', 'GEORGIA'),
	('GU', 'GUAM'),
	('HI', 'HAWAII'),
	('ID', 'IDAHO'),
	('IL', 'ILLINOIS'),
	('IN', 'INDIANA'),
	('IA', 'IOWA'),
	('KS', 'KANSAS'),
	('KY', 'KENTUCKY'),
	('LA', 'LOUISIANA'),
	('ME', 'MAINE'),
	('MD', 'MARYLAND'),
	('MA', 'MASSACHUSETTS'),
	('MI', 'MICHIGAN'),
	('MN', 'MINNESOTA'),
	('MS', 'MISSISSIPPI'),
	('MO', 'MISSOURI'),
	('MT', 'MONTANA'),
	('NE', 'NEBRASKA'),
	('NV', 'NEVADA'),
	('NH', 'NEW HAMPSHIRE'),
	('NJ', 'NEW JERSEY'),
	('NM', 'NEW MEXICO'),
	('NY', 'NEW YORK'),
	('NC', 'NORTH CAROLINA'),
	('ND', 'NORTH DAKOTA'),
	('OH', 'OHIO'),
	('OK', 'OKLAHOMA'),
	('OR', 'OREGON'),
	('PA', 'PENNSYLVANIA'),
	('PR', 'PUERTO RICO'),
	('RI', 'RHODE ISLAND'),
	('SC', 'SOUTH CAROLINA'),
	('SD', 'SOUTH DAKOTA'),
	('TN', 'TENNESSEE'),
	('TX', 'TEXAS'),
	('UT', 'UTAH'),
	('VT', 'VERMONT'),
	('VI', 'VIRGIN ISLANDS'),
	('VA', 'VIRGINIA'),
	('WA', 'WASHINGTON'),
	('WV', 'WEST VIRGINIA'),
	('WI', 'WISCONSIN'),
	('WY', 'WYOMING'),
)
# Define the home view
def home(request):
  count = Station.objects.all().count()
  return render(request, 'home.html', {'count': count})

# Create your views here.

class SearchResultsView(ListView):
    model = Station
    template_name = 'search_results.html'

    def get_queryset(self):
      query = self.request.GET.get("q")
      object_list = Station.objects.order_by('regular', 'midgrade', 'premium').filter(
        Q(name__icontains=query) | Q(zipcode__icontains=query) | Q(company__icontains=query)
      )
      return object_list


class StationCreate(LoginRequiredMixin, CreateView):
  model = Station
  fields = ['name', 'company', 'date', 'regular', 'midgrade', 'premium', 'cards_accepted', 'zipcode', 'street', 'city', 'state']
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
      error_message = (form.errors.as_text)

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class StationDelete(LoginRequiredMixin, DeleteView):
  model = Station
  success_url = '/stations/'


class PriceUpdate(LoginRequiredMixin, UpdateView):
  model = Station
  fields = ["regular", "midgrade", "premium"]

def stations_index(request):
  s = Station.objects.all()
  stations = reversed(s)
  return render(request, 'stations/index.html', {'stations': stations})


def stations_detail(request, station_id):
  station = Station.objects.get(id=station_id)
  stationName = station.name.replace(' ', '')
  strName = station.street.replace(' ', '')
  cityName = station.city.replace(' ', '')
  stateName = station.state.replace(' ', '')
  result = f"{stationName}+{strName},{cityName}+{stateName}"
  return render(request, 'stations/detail.html', {'station': station, 'result': result})

#elroy's function

#def toStr(station):
  #strName = station.street.replace(' ', '')
  #cityName = station.city.replace(' ', '')
  #stateName = station.state.replace(' ', '')
  #result = f"{strName},{cityName}+{stateName}"
  #reutrn result

def about(request):
  return render(request, 'about.html')


@login_required
def add_photo(request, station_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, station_id=station_id)
        except:
            print('We have an error here uploading to S3')
    return redirect('detail', station_id=station_id)

# def stationCount(request):
#   count = 4
#   return render(request, 'home.html', {'count': count})