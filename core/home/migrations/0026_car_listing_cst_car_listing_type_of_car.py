# Generated by Django 5.0 on 2023-12-09 11:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_remove_car_listing_cst_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_listing',
            name='cst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car_listing',
            name='type_of_car',
            field=models.CharField(default='', max_length=200),
        ),
    ]
