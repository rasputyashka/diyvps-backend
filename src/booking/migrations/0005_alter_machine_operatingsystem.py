# Generated by Django 5.1.3 on 2024-11-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_booked_alter_machine_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='operatingSystem',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
