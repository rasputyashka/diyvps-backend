# Generated by Django 5.1.3 on 2024-11-28 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_machine_operatingsystem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booked',
        ),
    ]
