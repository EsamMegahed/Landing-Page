# Generated by Django 5.1.7 on 2025-03-21 08:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hajj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='Hajj Images/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'webp', 'apng', 'avif', 'jpeg'])], verbose_name='Hajj Image')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Umrah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='Umrah Images/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'webp', 'apng', 'avif', 'jpeg'])], verbose_name='Umrah Image')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
