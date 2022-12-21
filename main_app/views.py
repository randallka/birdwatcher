from django.shortcuts import render


class Bird:  
  def __init__(self, species, location, description, number):
    self.species = species
    self.location = location
    self.description = description
    self.number = number

birds = [
  Bird('Cinnamon Teal', 'Cleveland National Forest, CA', 'Two females and one male seen feeding in a shallow pond', 3),
  Bird('Mourning Dove', 'Tulsa, Oklahoma', 'Group of doves spotted on the telephone pole in my neighborhood', 8),
  Bird('Chimney Swift', 'Greensboro, SC', 'Sighted flying over the river', 4),
  Bird('Ruby-throated Hummingbird', 'St Cloud, MN', 'Several birds have begun visiting our feeder', 6),
]

# Create your views here.
def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def birds_index(request): 
    #key in the dictionary is the variable name in the template 
    return render(request, 'birds/index.html', {'birds' : birds})