# Generated by Django 4.2.13 on 2024-05-19 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('place', models.CharField(blank=True, max_length=50, null=True)),
                ('linkedin_profile', models.CharField(blank=True, max_length=60, null=True)),
                ('insta_profile', models.CharField(blank=True, max_length=60, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
