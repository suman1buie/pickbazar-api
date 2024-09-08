# Generated by Django 4.2.13 on 2024-05-19 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('image_title', models.CharField(max_length=200)),
                ('catagory', models.CharField(choices=[('CASUAL', 'Casual'), ('DRAWING', 'Deawing'), ('CAMERA_CLICK', 'Camera Click'), ('ART', 'Art'), ('OTHERS', 'Others')], default='CAMERA_CLICK', max_length=50)),
                ('image', models.ImageField(upload_to='images//')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='users.artist')),
            ],
        ),
    ]
