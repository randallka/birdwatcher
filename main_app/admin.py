from django.contrib import admin

# Register your models here.
from .models import Bird
from .models import Sighting
admin.site.register(Bird)
admin.site.register(Sighting)