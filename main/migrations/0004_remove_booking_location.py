# Generated by Django 5.0.7 on 2024-07-20 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_booking_location_delete_location"),
    ]

    operations = [
        migrations.RemoveField(model_name="booking", name="location",),
    ]