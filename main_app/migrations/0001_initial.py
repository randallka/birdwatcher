# Generated by Django 4.1.4 on 2022-12-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
