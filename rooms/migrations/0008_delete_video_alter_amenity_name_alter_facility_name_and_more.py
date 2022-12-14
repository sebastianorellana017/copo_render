# Generated by Django 4.1.2 on 2022-10-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0007_remove_video_file_remove_video_room_alter_video_url"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Video",
        ),
        migrations.AlterField(
            model_name="amenity",
            name="name",
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name="facility",
            name="name",
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name="houserule",
            name="name",
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="name",
            field=models.CharField(max_length=80),
        ),
    ]
