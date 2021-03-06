# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20161227_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administered', models.BooleanField(default=False)),
                ('immunization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Immunization')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='vaccine',
            field=models.ManyToManyField(through='main.Schedule', to='main.Immunization'),
        ),
    ]
