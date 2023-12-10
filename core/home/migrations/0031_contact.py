# Generated by Django 5.0 on 2023-12-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_remove_car_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('user_name', models.CharField(blank=True, max_length=122, null=True)),
                ('email', models.CharField(blank=True, max_length=122, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('feedback', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
