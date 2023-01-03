from django.db import models
from django.urls import reverse
from mapbox_location_field.models import LocationField

STATUS = (
    ('M', 'Migratory'), 
    ('R', 'Residential')
)

# Create your models here.
class Bird(models.Model): 
    species = models.CharField(max_length=100)
    migratory = models.CharField("migratory/residential", max_length=1, choices=STATUS, default=STATUS[0][0])
    description = models.TextField(max_length=200)

    def get_absolute_url(self):   
        return reverse('show', kwargs={'bird_id': self.id})
        
class Location(models.Model):
    location = LocationField()
    description = models.TextField(max_length=200)
    birds = models.ManyToManyField(Bird)
    def get_absolute_url(self):
        return reverse('locations_show', kwargs={'pk': self.id})

class Sighting(models.Model):
    date = models.DateField('Date Seen') 
    time = models.TimeField()
    behavior = models.TextField(max_length=150)
    number = models.IntegerField(default='1')
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE) 
    class Meta: 
        ordering = ['date']

