# Generated by Django 4.2.7 on 2023-12-11 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_remove_notification_read_notification_notif_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car', to='home.share'),
        ),
    ]
