from django.shortcuts import render, redirect
from .models import Bird, Location
from .forms import SightingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})


def bird_show(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    sighting_form = SightingForm()
    return render(request, 'birds/show.html', {'bird': bird, 'sighting_form': sighting_form})


def add_sighting(request, bird_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.bird_id = bird_id
        new_sighting.save()
    return redirect('show', bird_id=bird_id)


class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'


class BirdUpdate(UpdateView):
    model = Bird
    fields = '__all__'


class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'


class LocationList(ListView):
    model = Location


class LocationShow(DetailView):
    model = Location

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bird_list'] = Bird.objects.all()
        return context


class LocationCreate(CreateView):
    model = Location
    fields = ['location', 'description']


class LocationUpdate(UpdateView):
    model = Location
    fields = ['location', 'description']


class LocationDelete(DeleteView):
    model = Location
    success_url = '/locations/'


def assoc_bird(request, location_id, bird_id):
    Location.objects.get(id=location_id).birds.add(bird_id)
    return redirect('locations_show', location_id)


def remove_bird(request, location_id, bird_id):
    Location.objects.get(id=location_id).birds.remove(bird_id)
    return redirect('locations_show', location_id)
