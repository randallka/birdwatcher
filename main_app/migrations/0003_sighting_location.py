# Generated by Django 4.1.4 on 2022-12-29 20:57

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_bird_location_remove_bird_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='location',
            field=mapbox_location_field.models.LocationField(default='null', map_attrs={}),
            preserve_default=False,
        ),
    ]
