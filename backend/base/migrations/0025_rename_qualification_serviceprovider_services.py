# Generated by Django 3.2.13 on 2022-06-29 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_serviceprovider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='qualification',
            new_name='services',
        ),
    ]
