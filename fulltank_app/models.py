from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

CARDS_ACCEPTED = (
  ('T', 'TRUE'),
  ('F', 'FALSE')
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


  def __str__(self):
    str = f"{self.name} on {self.date} is priced at {self.regular}, {self.midgrade}, {self.premium} id: {self.id}"
    if self.cards_accepted == 'TRUE':
      str = str + f" and they do accept card payments"
    else:
      str = str + f" and they do not accept card payments"
    return str

  def get_absolute_url(self):
    return reverse('detail', kwargs={'station_id': self.id})

