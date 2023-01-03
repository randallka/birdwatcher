from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='index'),
    path('birds/<int:bird_id>', views.bird_show, name='show'),
    path('birds/create/', views.BirdCreate.as_view(), name='birds_create'),
    #for update and delete params are expected to be named pk (primary key) = id
    path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='bird_update'),
    path('birds<int:pk>/delete/', views.BirdDelete.as_view(), name='bird_delete'),
    path('birds/<int:bird_id>/addsighting/', views.add_sighting, name='add_sighting'),
    path('locations/', views.LocationList.as_view(), name='location_index'),
    path('locations/<int:pk>/', views.LocationShow.as_view(), name='locations_show'),
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
    path('locations/<int:location_id>/assoc_bird/<int:bird_id>/', views.assoc_bird, name='assoc_bird'),
    path('locations/<int:location_id>/remove_bird/<int:bird_id>/', views.remove_bird, name='remove_bird'),
]

