# Generated by Django 3.2.13 on 2022-07-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_auto_20220717_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='details',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
