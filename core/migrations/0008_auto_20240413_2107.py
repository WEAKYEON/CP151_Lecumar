# Generated by Django 2.2.4 on 2024-04-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200510_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subimage_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='subimage_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='subimage_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='subimage_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
