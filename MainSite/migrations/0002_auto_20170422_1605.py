# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-22 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='Zdjecie',
            field=models.CharField(max_length=200),
        ),
    ]
