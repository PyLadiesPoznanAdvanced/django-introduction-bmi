# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-16 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('men', 'mężczyzna'), ('women', 'kobieta')], max_length=20)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
            ],
        ),
    ]