# Generated by Django 4.2.6 on 2023-12-09 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_car_listing_type_of_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_listing',
            name='cst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]