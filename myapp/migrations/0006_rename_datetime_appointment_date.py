# Generated by Django 5.1.3 on 2024-11-19 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_date_appointment_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='dateTime',
            new_name='date',
        ),
    ]
