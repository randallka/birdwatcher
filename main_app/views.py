from django.shortcuts import render
from .models import Bird
# import class-based views 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def birds_index(request): 
  birds = Bird.objects.all()
  #key in the dictionary is the variable name in the template 
  return render(request, 'birds/index.html', {'birds' : birds})

def bird_show(request, bird_id): 
  bird = Bird.objects.get(id=bird_id)
  return render(request, 'birds/show.html', {'bird' : bird})

# class based view (create)

class BirdCreate(CreateView): 
  model = Bird
  fields = '__all__'
class BirdUpdate(UpdateView): 
  model = Bird
  fields = ['location', 'description', 'number']
class BirdDelete(DeleteView): 
  model = Bird 
  success_url = '/birds/'