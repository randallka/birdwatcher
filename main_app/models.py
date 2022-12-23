from django.db import models
from django.urls import reverse

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


class Sighting(models.Model):
    date = models.DateField('Date Seen') 
    time = models.TimeField()
    behavior = models.TextField(max_length=150)
    number = models.IntegerField(default='1')
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE) 
    class Meta: 
        ordering = ['date']