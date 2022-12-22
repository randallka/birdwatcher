from django.db import models
from django.urls import reverse

# Create your models here.
class Bird(models.Model): 
    species = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    number = models.IntegerField()

    def get_absolute_url(self):   
        return reverse('detail', kwargs={'bird_id': self.id})