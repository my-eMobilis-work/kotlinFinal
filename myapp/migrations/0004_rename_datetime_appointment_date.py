# Generated by Django 5.1.3 on 2024-11-18 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_appointment_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='dateTime',
            new_name='date',
        ),
    ]