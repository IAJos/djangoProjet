# Generated by Django 5.1.1 on 2024-09-18 23:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('sold', models.BooleanField(default=False)),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)])),
                ('type', models.CharField(choices=[('R', 'Records'), ('C', 'Clothing'), ('P', 'Posters'), ('M', 'Misc')], max_length=5, null=True)),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band')),
            ],
        ),
    ]
