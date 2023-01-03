from django.forms import ModelForm
from django import forms
from .models import Sighting
from .models import Location
# instantiating this class will create a form from our feeding model
class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput): 
    input_type = 'time'

class SightingForm(ModelForm): 
    class Meta: 
        model = Sighting
        fields = ['date', 'time', 'behavior', 'number']
        widgets = { 
            'date' : DateInput(),
            'time' : TimeInput(), 
        }
