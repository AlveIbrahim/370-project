# Generated by Django 4.2.7 on 2023-11-27 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_car_listing_rename_nid_customer_customer_nid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Name',
        ),
    ]
