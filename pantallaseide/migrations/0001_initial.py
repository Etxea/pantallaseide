# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=b'imgenes/')),
                ('orden', models.DecimalField(decimal_places=0, default=1, max_digits=2)),
                ('carrusel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantallaseide.Carrusel')),
            ],
        ),
        migrations.CreateModel(
            name='Pantalla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='carrusel',
            name='pantalla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pantallaseide.Pantalla'),
        ),
    ]
