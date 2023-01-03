from django.contrib import admin

# Register your models here.
from .models import Bird
from .models import Sighting
from .models import Location
from mapbox_location_field.admin import MapAdmin  
admin.site.register(Bird)
admin.site.register(Sighting)
admin.site.register(Location, MapAdmin)
