# Generated by Django 4.2.6 on 2023-12-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_share_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_listing',
            name='type_of_car',
            field=models.CharField(default='', max_length=200),
        ),
    ]
