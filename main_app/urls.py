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
]