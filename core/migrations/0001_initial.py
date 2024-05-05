# Generated by Django 5.0.2 on 2024-04-21 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=20, verbose_name='Sub titulo')),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='image', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizacion')),
            ],
        ),
    ]
