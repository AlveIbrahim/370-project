# Generated by Django 4.2.7 on 2023-11-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Adress',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Nid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phn',
            field=models.CharField(default='', max_length=11),
        ),
    ]
