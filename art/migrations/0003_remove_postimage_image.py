# Generated by Django 4.2.13 on 2024-08-31 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_postimage_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimage',
            name='image',
        ),
    ]
