# Generated by Django 5.0 on 2023-12-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_payment_inf'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.AddField(
            model_name='car_listing',
            name='customer_licence',
            field=models.ImageField(blank=True, null=True, upload_to='cimage/'),
        ),
    ]