# Generated by Django 2.2.4 on 2019-09-12 02:38

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taroudant_etabs', '0002_auto_20190912_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='etablissements',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, srid=4326),
        ),
    ]
