# Generated by Django 5.0 on 2023-12-10 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_remove_car_listing_has_car_car_listing_has_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='info',
        ),
    ]