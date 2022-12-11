# Generated by Django 4.1.2 on 2022-10-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_amenity_name_alter_facility_name_and_more'),
        ('lists', '0002_list_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='rooms',
            field=models.ManyToManyField(blank=True, related_name='lists', to='rooms.room'),
        ),
    ]
