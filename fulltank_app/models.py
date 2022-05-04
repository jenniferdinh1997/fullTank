from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

CARDS_ACCEPTED = (
  ('T', 'TRUE'),
  ('F', 'FALSE')
)

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

class Station(models.Model):
  name = models.CharField(max_length = 100)
  company = models.CharField(max_length = 100)
  date = models.DateField('Date Of Visit')
  regular = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(20.0)])
  midgrade = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(20.0)])
  premium = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(20.0)])
  cards_accepted = models.CharField(
    max_length = 1,
      choices = CARDS_ACCEPTED,
      default = CARDS_ACCEPTED[0][0]
  )
  zipcode = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  street = models.CharField(max_length = 100, null=True)
  city = models.CharField(max_length = 100, null=True)
  state = models.CharField(
    max_length = 2,
    choices = STATES,
    default = STATES[0][0]
  )


  def __str__(self):
    str = f"{self.name} at {self.street} on {self.date} is priced at {self.regular}, {self.midgrade}, {self.premium} id: {self.id}"
    if self.cards_accepted == 'TRUE':
      str = str + f" and they do accept card payments"
    else:
      str = str + f" and they do not accept card payments"
    return str

  def get_absolute_url(self):
    return reverse('detail', kwargs={'station_id': self.id})

