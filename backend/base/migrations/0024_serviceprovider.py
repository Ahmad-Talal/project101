# Generated by Django 3.2.13 on 2022-06-29 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0023_auto_20220628_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('fee', models.IntegerField(blank=True, default=0, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=20, max_digits=27, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=20, max_digits=27, null=True)),
                ('qualification', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='/def.jpg', null=True, upload_to='')),
                ('experience', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('User', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]