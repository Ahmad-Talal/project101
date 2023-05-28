# Generated by Django 3.2.13 on 2022-06-28 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_rename_experience_rescue_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='details',
        ),
        migrations.AddField(
            model_name='appointment',
            name='vet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.vet'),
        ),
    ]
