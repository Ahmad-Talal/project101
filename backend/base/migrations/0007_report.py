# Generated by Django 3.2.6 on 2022-02-11 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rescue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('phonenumber', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
