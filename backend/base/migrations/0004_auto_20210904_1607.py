# Generated by Django 3.2.6 on 2021-09-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/def.jpg', null=True, upload_to=''),
        ),
    ]
